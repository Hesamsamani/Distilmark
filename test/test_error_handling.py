# -*- coding: utf-8 -*-
"""Regression tests: input-PDF problems must surface as clean, typed errors
(``converters.PdfError``) with human-readable messages — never as raw PyMuPDF /
pdfminer exceptions or Python tracebacks in the UI.

Fixtures (committed in this folder):
  * ``pw.pdf``    — a password-protected / encrypted PDF
  * ``empty.pdf`` — a 23-byte non-PDF (corrupt / not a real PDF)

Runnable directly (``python test/test_error_handling.py``) or via pytest.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))  # repo root, so `distilmark` imports when run directly

from distilmark import converters  # noqa: E402
from distilmark.converters import ConvertOptions  # noqa: E402
ENCRYPTED = HERE / "pw.pdf"
MALFORMED = HERE / "empty.pdf"


def _assert_pdferror(fn, must_contain):
    try:
        fn()
    except converters.PdfError as e:
        msg = str(e).lower()
        assert must_contain in msg, f"expected {must_contain!r} in message, got: {e}"
        return
    except Exception as e:  # noqa: BLE001
        raise AssertionError(
            f"expected converters.PdfError, got {type(e).__name__}: {e}"
        )
    raise AssertionError("expected converters.PdfError, but no error was raised")


def test_native_encrypted():
    _assert_pdferror(
        lambda: converters.convert_native(ENCRYPTED, ConvertOptions(), None),
        "password",
    )


def test_native_malformed():
    _assert_pdferror(
        lambda: converters.convert_native(MALFORMED, ConvertOptions(), None),
        "valid pdf",
    )


def test_pdfplumber_encrypted():
    _assert_pdferror(
        lambda: converters.convert_pdfplumber(ENCRYPTED, ConvertOptions(), None),
        "password",
    )


def test_pdfplumber_malformed():
    _assert_pdferror(
        lambda: converters.convert_pdfplumber(MALFORMED, ConvertOptions(), None),
        "valid pdf",
    )


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"[PASS] {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"[FAIL] {t.__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    raise SystemExit(1 if failed else 0)
