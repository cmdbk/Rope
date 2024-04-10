datas = []
datas += collect_data_files('Rope.locales')

block_cipher = None

a = Analysis([
        'Rope.py',
        ],
    pathex=[
        './rope',
        ],
    binaries=[],
    datas=datas
    hiddenimports=[
        'numpy',
        'opencv-python',
        'scikit-image',
        'pillow',
        'onnx',
        'onnxruntime',
        'protobuf',
        'tqdm',
        'ftfy',
        'regex',
        'scikit-image',
        'tk',
        'urllib3',
        'opencv-contrib-python',
        'ffmpeg',
        'torch',
        'torchvision',
        'torchaudio',
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
app = BUNDLE(coll,
             name='Rope.app',
             icon='ico.icns',
             bundle_identifier=None,
             info_plist={
                'NSHighResolutionCapable': 'True'
             }
)
