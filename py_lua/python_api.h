#include <Python.h>
#include <unistd.h>
#include <dlfcn.h>
#include <string.h>

int downloadBitstream();
void  *startHdmi();
void getCurrentFrame(Py_buffer *view);
unsigned char * getFrameBuffer();
void pyinit() __attribute__((constructor));
void pyfinal() __attribute__((constructor));