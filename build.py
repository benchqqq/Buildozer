from pythonforandroid.toolchain import APKBuild

   APKBuild(
       name="myapp",
       version="1.0",
       package="org.test.myapp",
       source_dir=".",
       requirements="kivy",
       android_api=30,
       ndk_version="23b",
       arch="armeabi-v7a",
   )
