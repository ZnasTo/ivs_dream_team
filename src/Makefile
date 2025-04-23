##Sample Makefile
# @author xturcam00 Martin Turčan
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

.PHONY: clean test pack stddev run doc all

test:
	$(PC) $(TESTS)

clean:
	@echo Removing files:
	@for %%f in ($(DELETE_FILES)) do @echo "  Deleting file: %%f" && del /q "..\%%f"
	@echo Removing directories:
	@for %%d in ($(DELETE_DIRS)) do @echo "  Deleting directory: %%d" && rmdir /s /q "..\%%d"
	@echo Cleaning plan/ directory 
	@for %%f in ("..\plan\*") do @if not "%%~nxf"=="xrecmaa00_xturcam00_xkubisa00_xkovacj00_plan.txt" del /q /f "%%f" >nul 2>&1
	@for /d %%d in ("..\plan\*") do @rmdir /s /q "%%d" >nul 2>&1
	@echo Cleaning profiling directory
	@for %%f in ("..\profiling\*") do @if not "%%~nxf"=="zprava.pdf" del /q /f "%%f" >nul 2>&1
	@for /d %%d in ("..\profiling\*") do @rmdir /s /q "%%d" >nul 2>&1
	@echo Cleaning src directory
	@for %%f in (*) do @if not "%%~nxf"=="Makefile" if not "%%~nxf"=="Doxyfile" if not "%%~xf"==".py" del /q /f "%%f" >nul 2>&1
	@for /d %%d in (*) do @rmdir /s /q "%%d" >nul 2>&1
	@echo Cleaning mockup directory 
	@for %%f in ("..\mockup\*") do @if not "%%~nxf"=="mockup.png" del /q /f "%%f" >nul 2>&1
	@for /d %%d in ("..\mockup\*") do @rmdir /s /q "%%d" >nul 2>&1
	@echo Done.

stddev: $(BAT_FILE)

$(BAT_FILE):
	@echo off > $(BAT_FILE)
	@echo python $(PYTHON_SCRIPT) %* >> $(BAT_FILE)


pack: clean
	powershell -Command "compress-archive -Path ".." -DestinationPath "..\DreamTeam.zip""

run: 
	python gui_calculator.py

doc:
	doxygen

all: stddev
	@echo Build process completed successfully.



