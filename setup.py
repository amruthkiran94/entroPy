#encoding=utf-8
from distutils.core import setup, Extension  
import glob

setup (name = 'entroPy',
       version = '0.1.0',
       description='maximum entropy (MaxEnt) classifier',
       author='xiaolong,zeng',
       author_email='zengxiaolong2015@163.com',
       ext_modules =[Extension('_model',include_dirs = ['c'],sources=['_model.c']+glob.glob('c/*.c'))],
       ext_package='entroPy',
       packages=['entroPy'],
       package_dir={'entroPy':'py'},
       license = 'GNU GPL version 3',
       classifiers=[
                    'Development Status :: 5 - Production/Stable',
                    'Intended Audience :: Science/Research',
                    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                    'Operating System :: OS Independent',
                    'Programming Language :: C',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 3',
                    'Topic :: Scientific/Engineering'
                    ]
       ) 
