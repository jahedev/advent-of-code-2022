
default:
	echo Makefile to clean output files

clean:
	find . -type f -name '*.o' -delete
	find . -type f -name '*.out' -delete
	find . -type f -name '*.class' -delete