ffi = require('ffi')
image = require('image')

ffi.cdef[[                                                                                        
void downloadBitstream();                                                                     
]]
ffi.cdef[[
void  *startHdmi();
]]
ffi.cdef[[
int getFrameBuffer();
]]

ptr = ffi.new('int')
clib = ffi.load('/home/xpp/code/out.so')
clib.downloadBitstream()
clib.startHdmi()

ptr = clib.getFrameBuffer()
--x=torch.FloatStorage(6220800,ptr)
x = torch.FloatStorage(921600,tonumber(ptr))
y = torch.FloatTensor(x)
img = torch.reshape(y,torch.LongStorage{3,640,480})
image.display(img)
--qlua -e "require('trepl')()"