SOURCE = python_api.c

INC= -I /home/xpp/torch/pkg/torch/lib/TH/ -I /usr/include/python3.4m -I /home/xpp/torch/install/include/TH/
LIBS= -lpthread -ldl -lutil -lm -lpython3.4m

all:
	gcc -c $(SOURCE) -o test $(INC) 
	gcc test -Wl,--start-group $(LIBS) -Xlinker -export-dynamic -Wl,--end-group -o out

shared:
	gcc -c  -O3 -Ofast -fPIC $(SOURCE) -o test $(INC)
	gcc -O3 -Ofast -shared $(INC) -fPIC -rdynamic test -Wl,--start-group $(LIBS) -Xlinker -export-dynamic -Wl,--end-group -o out.so
	rm test
