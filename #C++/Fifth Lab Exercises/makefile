all:05

05: 05_05.o Split.o Element.o
	g++ -o 05 05_05.o Split.o Element.o

05_05.o: 05_05.cpp Element.h Split.h
	g++ -c 05_05.cpp Element.h Split.h

Element.o: Element.cpp
	g++ -c Element.cpp


