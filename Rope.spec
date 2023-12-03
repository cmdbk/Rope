# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


    a = Analysis([
    'Rope.py',
    ],
    pathex=[],
    binaries=[],
    datas=[
    (‘benchmark’, ‘./benchmark'),
    ('models', './models'),
    ('Rope', './rope'),
    ('Venv', './env'),
    ],
    hiddenimports=[
    'numpy'
    'opencv-python'
    'scikit-image'
    'tk'
    'pillow==9.5.0'
    'onnx'
    'onnxruntime'
    'protobuf'
    'torch'
    'torchvision'
    'torchaudio'
    'urllib3'
    'tqdm'
    'ftfy'
    'regex'
    'opencv-contrib-python'
    'ffmpeg'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Rope',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Rope',
)
app = BUNDLE(
    coll,
    name='Rope.app',
    icon='icons/icon.icns',
    bundle_identifier=None,
    info_plist={
        'CFBundleDisplayName': 'Rope',
        'CFBundleName': 'Rope',
        'CFBundlePackageType': 'APPL',
        'CFBundleSignature': 'BATR',
        'CFBundleShortVersionString': version,
        'CFBundleVersion': version,
        'CFBundleExecutable': 'Rope',
        'CFBundleIconFile': 'icon.icns',
        'CFBundleIdentifier': 'dev.Hillobar.batr',
        'CFBundleInfoDictionaryVersion': '6.0',
        'LSApplicationCategoryType': 'public.app-category.graphics-design',
        'LSEnvironment': {'LANG': 'zh_CN.UTF-8'},
      }
)
