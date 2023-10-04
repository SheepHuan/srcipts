import os

def compile_command(save_path):
    f = open(save_path,"w")
    if not os.path.exists(source_path):
        cmd = f"git clone --recursive -b {tag} https://github.com/Microsoft/onnxruntime.git {source_path}"
        f.write(cmd+"\n")
    cmd = f"cd {source_path}"
    f.write(cmd+"\n")
    if target=="windows":
        cmd = f"./build.bat --config RelWithDebInfo --build_shared_lib --parallel --skip_submodule_sync  --cmake_generator \"Visual Studio 17 2022\""
    else:
        cmd = f"./build.sh --config RelWithDebInfo --build_shared_lib --parallel --skip_submodule_sync --cmake_generator \"Unix Makefiles\""
    f.write(cmd+"\n")

if __name__=="__main__":
    # ndk_path="D:/env_library/android_sdk/ndk/26.0.10792818"
    # install_path="D:/code/transsion/srcipts/3rd-party/install/onnxruntime"
    # source_path="D:/code/transsion/srcipts/3rd-party/onnxruntime"
    # build_path="D:/code/transsion/srcipts/build/onnxruntime"
    # target="windows" # windows, linux_aarch64, android
    # tag = "v1.16.0"
    # newline="`"
    # compile_command(f"generated/onnxruntime@{tag}_{target}.ps1")
 
    tag = "v1.16.0"

    install_path=f"/home/yanghuan/Code/install/onnxruntime@{tag}"
    source_path=f"/home/yanghuan/Code/onnxruntime@{tag}"
    build_path="/tmp/onnxruntime"
    target="linux" # windows, linux_aarch64, android
   
    newline="`"
    compile_command(f"generated/onnxruntime@{tag}_{target}.sh")