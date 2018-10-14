@echo off
set opt=
:looparg
if (%1) == () goto endloop
set arg=%1
if %arg:~0,2%==f- (
    set opt=%opt% -Dfile=%arg:~2%
) else if %arg:~0,2%==p- (
    set opt=%opt% -Dfolder=%arg:~2%
) else (
    set opt=%opt% %arg%
)
shift
goto looparg
:endloop
set opt=%opt:~1%
@echo on
ant -Dsandbox=sand -propertyfile ./properties/build-sand.properties %opt%