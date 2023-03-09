#pragma once

#ifdef _WIN32
  #define lib2_EXPORT __declspec(dllexport)
#else
  #define lib2_EXPORT
#endif

lib2_EXPORT void lib2();
