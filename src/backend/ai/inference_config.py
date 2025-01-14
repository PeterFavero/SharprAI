import sys
import os

sys.path.append("/workspace/tensorrt/")
import vapoursynth as vs

core = vs.core
vs_api_below4 = vs.__api_version__.api_major < 4
core.num_threads = 8

core.std.LoadPlugin(path="/usr/local/lib/libvstrt.so")


def inference_clip(video_path="", clip=None):
    clip = core.bs.VideoSource(source=video_path)

    clip = vs.core.resize.Bicubic(clip, format=vs.RGBH, matrix_in_s="709")  # RGBS means fp32, RGBH means fp16
    clip = core.trt.Model(
        clip,
        engine_path="/workspace/tensorrt/AnimeJaNai_V2_Compact_36k_op18_fp16_clamp.engine",  # read readme on how to build engine
        num_streams=2,
    )
    clip = vs.core.resize.Bicubic(clip, format=vs.YUV420P8, matrix_s="709")  # you can also use YUV420P10 for example

    return clip