import os
import shutil



def compile_command_for_android(save_path):
    
    f = open(save_path,"w")
    if not os.path.exists(source_path):
        cmd = f"git clone --recursive -b 4.8.0 https://github.com/opencv/opencv.git {source_path}\n"
        f.write(cmd)
    if os.path.exists(build_path):
        shutil.rmtree(build_path)
    if os.path.exists(install_path):
        shutil.rmtree(install_path)
    cmd = f"""
cmake -DCMAKE_TOOLCHAIN_FILE={ndk_path}/build/cmake/android.toolchain.cmake {newline}
-DCMAKE_ANDROID_NDK=ANDROID_NDK {newline}
-DANDROID_NATIVE_API_LEVEL=29 {newline}
-DBUILD_ANDROID_PROJECTS=OFF {newline}
-DBUILD_ANDROID_EXAMPLES=OFF {newline}
-DCMAKE_BUILD_TYPE=Release  {newline}
-DBUILD_JAVA=OFF  {newline}
-DBUILD_ANDROID_PROJECTS=OFF {newline}
-DBUILD_DOCS=off {newline}
-DBUILD_FAT_JAVA_LIB=off {newline}
-DBUILD_opencv_calib3d=off {newline}
-DBUILD_opencv_contrib=off {newline}
-DBUILD_opencv_features2d=off {newline}
-DBUILD_opencv_flann=off {newline}
-DBUILD_opencv_gpu=off {newline}
-DBUILD_opencv_java=off {newline}
-DBUILD_opencv_legacy=off {newline}
-DBUILD_opencv_ml=off {newline}
-DBUILD_opencv_nonfree=off {newline}
-DBUILD_opencv_objdetect=off {newline}
-DBUILD_opencv_ocl=off {newline}
-DBUILD_opencv_photo=off {newline}
-DBUILD_opencv_python=off {newline}
-DBUILD_opencv_stitching=off {newline}
-DBUILD_opencv_superres=off {newline}
-DBUILD_opencv_ts=off {newline}
-DBUILD_PERF_TESTS=OFF {newline}
-DBUILD_TESTS=OFF {newline}
-DBUILD_opencv_dnn=off {newline}
-DWITH_1394=off {newline}
-DWITH_EIGEN=off {newline}
-DWITH_FFMPEG=off {newline}
-DWITH_GIGEAPI=off {newline}
-DWITH_GSTREAMER=off {newline}
-DWITH_GTK=off {newline}
-DWITH_PVAPI=off {newline}
-DWITH_V4L=off {newline}
-DWITH_LIBV4L=off {newline}
-DWITH_CUDA=off {newline}
-DWITH_CUFFT=off {newline}
-DWITH_OPENCL=off {newline}
-DWITH_OPENCLAMDBLAS=off {newline}
-DWITH_OPENCLAMDFFT=off {newline}
-DBUILD_opencv_world=on {newline}
-DANDROID_ABI=arm64-v8a {newline}
-DANDROID_STL=c++_shared {newline}
-DBUILD_SHARED_LIBS=ON {newline}
-DCMAKE_INSTALL_PREFIX={install_path} {newline}
-S {source_path} {newline}
-B {build_path} {newline}
-G Ninja \n
"""
    f.write(cmd)
    cmd = f"cmake --build {build_path}\n"
    f.write(cmd)
    cmd = f"cmake --install {build_path}\n"
    f.write(cmd)


if __name__=="__main__":
    ndk_path="D:/env_library/android_sdk/ndk/26.0.10792818"
    install_path="D:/code/transsion/srcipts/3rd-party/install/opencv"
    source_path="D:/code/transsion/srcipts/3rd-party/opencv"
    build_path="D:/code/transsion/srcipts/build/opencv"
    tag = "4.8.0"
    newline="`"
    compile_command_for_android("generated/opencv_android.ps1")

    
