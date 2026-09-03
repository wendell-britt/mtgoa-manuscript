# -*- coding: utf-8 -*-
"""
profile.py — the loader for editorial.yaml, the per-project profile.

One small accessor used by gate.py, telling.py, trailing_and.py, light_verb.py and
coherence.py. Every getter takes the caller's current hardcoded value as `default`, so a
missing manifest, a missing key, or a missing PyYAML changes nothing: the instrument keeps its
built-in value and the pipeline runs exactly as before. The manifest is authoritative when
present and invisible when absent, which is what makes the refactor non-breaking.

See specs/EDITORIAL_PIPELINE_COHERENCE_2026-09-03.md for the universal/profile split.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
MANIFEST = os.path.join(ROOT, "editorial.yaml")

_cache = None


def _load():
    global _cache
    if _cache is not None:
        return _cache
    try:
        import yaml
        with open(MANIFEST, encoding="utf-8") as fh:
            _cache = yaml.safe_load(fh) or {}
    except Exception:
        _cache = {}
    return _cache


def exists():
    return os.path.exists(MANIFEST)


def path():
    return MANIFEST


def baseline(name, default):
    try:
        return float(_load().get("baselines", {}).get(name, default))
    except Exception:
        return default


def baselines(default=None):
    v = _load().get("baselines")
    return dict(v) if v else dict(default or {})


def banned(default):
    v = _load().get("banned")
    return list(v) if v else list(default)


def corpus(default):
    v = _load().get("corpus")
    return list(v) if v else list(default)


def pass_list(default=None):
    v = _load().get("pass")
    return list(v) if v else list(default or [])


def project_only(default=None):
    v = _load().get("project_only")
    return list(v) if v else list(default or [])
