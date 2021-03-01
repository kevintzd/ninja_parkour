# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

SETUP_DIR = 'D:\\Desktop\\ninja_parkour\\ninja_parkour\\resources'
a = Analysis(['D:\\Desktop\\ninja_parkour\\ninja_parkour\\main.py',
            'D:\\Desktop\\ninja_parkour\\ninja_parkour\\map.py',
            'D:\\Desktop\\ninja_parkour\\ninja_parkour\\loadResource.py',
            'D:\\Desktop\\ninja_parkour\\ninja_parkour\\game_control.py',
            'D:\\Desktop\\ninja_parkour\\ninja_parkour\\configurations.py',
            'D:\\Desktop\\ninja_parkour\\ninja_parkour\\character.py',
            'D:\\Desktop\\ninja_parkour\\ninja_parkour\\scenes\\credits.py',
            'D:\\Desktop\\ninja_parkour\\ninja_parkour\\scenes\\game_over.py',
            'D:\\Desktop\\ninja_parkour\\ninja_parkour\\scenes\\introduction.py',
            'D:\\Desktop\\ninja_parkour\\ninja_parkour\\scenes\\scene.py',
            'D:\\Desktop\\ninja_parkour\\ninja_parkour\\scenes\\StartingMenu.py'],
             pathex=['D:\\Desktop\\ninja_parkour\\ninja_parkour'],
             binaries=[],
             datas=[(SETUP_DIR, 'resources')],
             hiddenimports=['pygame', 'itertool'],
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
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
