#pragma once

#ifdef _WIN32
  #define mainproject_EXPORT __declspec(dllexport)
#else
  #define mainproject_EXPORT
#endif

mainproject_EXPORT void mainproject();
