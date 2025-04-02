#Sample Makefile
## @author xturcam00 Martin Turčan
#
# File contains makefile

PC = python
TESTS = tests.py
BAT_FILE = stddev.bat
PYTHON_SCRIPT = profiling.py


KEEP_FILES := README.md dokumentace.pdf debugging.png screenshot.png skutecnost.txt hodnoceni.txt .gitignore .editorconfig 
KEEP_DIRS := mockup plan src profiling .git

ALL_FILES := $(shell dir /b /a-d ..\)
ALL_DIRS := $(shell dir /b /ad ..\)

DELETE_FILES := $(filter-out $(KEEP_FILES), $(ALL_FILES))
DELETE_DIRS := $(filter-out $(KEEP_DIRS), $(ALL_DIRS))

.PHONY: clean test pack stddev

test:
	$(PC) $(TESTS)

clean:
	@echo "Removing files:"
	@for %%f in ($(DELETE_FILES)) do @echo "  Deleting file: %%f" && del /q "..\%%f"
	@echo "Removing directories:"
	@for %%d in ($(DELETE_DIRS)) do @echo "  Deleting directory: %%d" && rmdir /s /q "..\%%d"
	@echo "Cleanup complete."
	@echo "Cleaning plan/ directory (keeping only x.txt)"
    

stddev: $(BAT_FILE)

$(BAT_FILE):
	@echo off > $(BAT_FILE)
	@echo python $(PYTHON_SCRIPT) %* >> $(BAT_FILE)

pack:
	powershell -Command "compress-archive -Path ".." -DestinationPath "..\fero""



