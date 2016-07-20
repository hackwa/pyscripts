all:
	gcc -c python_api.c -o test -I/usr/include/python3.4m -I/usr/include/python3.4m 
	gcc test -Wl,--start-group -L/opt/lib/python3.4/config-3.4m -lpthread -ldl -lutil -lm -lpython3.4m -Xlinker -export-dynamic -Wl,--end-group -o out
