#include <Python.h>
#include <unistd.h>
#include <dlfcn.h>
#include <string.h>

#define videoHeight 480
#define videoWidth 640
#define videoSize videoHeight*videoWidth*3

int downloadBitstream();
void  *startHdmi();
void getCurrentFrame(Py_buffer *view);
int getFrameBuffer();
void pyinit() __attribute__((constructor));
void pyfinal() __attribute__((destructor));