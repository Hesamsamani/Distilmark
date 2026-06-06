# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('icon.png', '.')]
binaries = []
hiddenimports = []
tmp_ret = collect_all('pymupdf')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('pymupdf4llm')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('pdfplumber')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

# Exclude heavy ML / data-science packages that are NOT required by Distilmark
# (the build machine's site-packages often contains torch, sklearn, tensorflow etc.
# from other projects; bundling them makes the .exe 4-5x larger and slower to start).
excludes = [
    'torch', 'torchvision', 'torchaudio',
    'tensorflow', 'tensorflow-cpu', 'tensorflow-intel',
    'sklearn', 'scikit-learn',
    'pandas',
    'matplotlib', 'matplotlib.pyplot',
    'scipy',
    'cv2', 'opencv-python',
    'transformers',
    'numba',
    'onnxruntime', 'onnxruntime-gpu',
    'sympy',
    'jupyter', 'notebook', 'IPython',
    'tensorboard',
    'PIL.ImageQt',  # not needed; we use Qt directly
]

a = Analysis(
    ['distilmark_launcher.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludes,
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Distilmark',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
