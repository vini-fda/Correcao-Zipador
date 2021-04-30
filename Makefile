give_permission:
	chmod +x ./zipador.sh
run: give_permission
	python3 main.py
clean:
	rm -r zipador_test*