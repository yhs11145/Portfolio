# -*- mode: python -*-

block_cipher = None


a = Analysis(['playauto.py'],
             pathex=['C:\\Users\\yhs11\\OneDrive\\����\\work\\�÷��̿���2.0\\���α׷�'],
             binaries=[('chromedriver.exe', '.')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='playauto',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
