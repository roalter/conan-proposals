#pragma once

#ifdef _WIN32
  #define lib1_EXPORT __declspec(dllexport)
#else
  #define lib1_EXPORT
#endif

lib1_EXPORT void lib1();
