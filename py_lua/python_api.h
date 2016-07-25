#include <Python.h>
#include <unistd.h>

int downloadBitstream();
void  *startHdmi();
void getCurrentFrame(Py_buffer *view);
unsigned char * getFrameBuffer();
