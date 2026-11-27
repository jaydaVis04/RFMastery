.PHONY: start setup doctor map test validate validate-starters validate-hdl
start:
	python3 learn
setup:
	python3 learn setup
doctor:
	python3 learn doctor
map:
	python3 learn map
test:
	python3 -m unittest discover -s tests -v
validate:
	python3 tools/validate_course.py
validate-starters:
	python3 tools/validate_course.py --starters
validate-hdl:
	python3 tools/validate_course.py --require-hdl
