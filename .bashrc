ulimit -s 10000

# === BASIC RUN SCRIPT === #

function compile {
    # Compile a cpp program with standard compile flags.
    # Usage: compile <cpp_file> <output_path>
    g++ $1 -g -std=c++14 -Wall -Wextra -Wconversion -Wshadow -Wfatal-errors -fsanitize=address,undefined -o $2
}

function runcompiled {
    # Run a script (python or c) with some file provided input
    # Usage: runcompiled <script_file> <input_file>
    if [[ $1 == *.py ]]; then
        { time (python3 $1 <$2 >o 2>error) >/dev/null; } 2>timing
    else
        { time (./$1 <$2 >o 2>error) >/dev/null; } 2>timing
    fi
    cat timing | grep real | awk '{print $2}'
    cat error
    rm timing
    rm error
    diff -y o ${2%in}[ao]?? >t || cat t || cat o
    rm o
    rm t
}

function run {
    # Run a script against all/some tests in a directory.
    # Usage:
    #   run
    #       - Run the first found script against all files matching tests/*.in
    #   run jackson.py
    #       - Run jackson.py against all files matching tests/*.in
    #   run jackson.cpp tests/3.in
    #       - Run jackson.cpp against tests/3.in

    clear;clear
    first_file=`ls -t *.{cpp,py} | head -n1`
    F=${1-$first_file}
    if [[ $F == *.c* ]]
    then
        compile $F sol
        runner='sol'
    else
        runner=$F
    fi
    if [ -n "$2" ]; then
        echo ---$F $2
        runcompiled $runner $2
    else
        for i in tests/*.in; do
            echo ---$F $i
            runcompiled $runner $i
        done
    fi
}

# === FILE/FOLDER CREATION === #

function makefile {
    # Make a file in this directory, copying from the template files.
    # Usage: makefile jackson.py
    if [[ $1 == *.c* ]]
    then
        search="c_template.cpp"
    else
        search="python_template.py"
    fi
    path="$search"
    for i in {1..10}
    do
        if test -f "$path"; then
            cp "$path" $1
            echo "Created $1 from $path"
            break
        else
            path="../$path"
        fi
    done
}

function makedirs {
    # Make directories for each problem letter.
    # Usage: makedirs F
    for i in  $( eval echo {A..$1} ); do
        # Create subdir
        mkdir $i
        mkdir "$i/tests"
    done
}


# === EXTENDED FUNCTIONALITY === #

function runtests {
    # Run tests with a test generator and compare two solutions
    # Useful if you have an inefficient version which is guaranteed correct, and you want to test the optimised version
    # Test generator should randomly output a single test case to stdout.
    # Arguments
        # Test generator
        # Correct script
        # Test script
        # Total tests
    clear;clear
    if [[ $2 == *.c* ]];
    then
        compile $2 correct
    fi
    if [[ $3 == *.c* ]];
    then
        compile $3 test
    fi
    ITERATIONS=${4:-50}
    completed=1
    for (( i=1; i<=ITERATIONS; i++ )) do
        echo "Test #$i"
        python3 $1 > test.in
        if [[ $2 == *.c* ]];
        then
            ./correct < test.in > test.out
        fi
        if [[ $2 == *.py ]];
        then
            python3 $2 < test.in > test.out
        fi
        error=$?
        if [[ $error -ne 0 ]]
        then
            echo "Error on test case with truth script"
            completed=0
            break
        fi
        if [[ $3 == *.c* ]];
        then
            ./test < test.in > test.cmp
        fi
        if [[ $3 == *.py ]];
        then
            python3 $3 < test.in > test.cmp
        fi
        error=$?
        if [[ $error -ne 0 ]]
        then
            echo "Error on test case with test script"
            completed=0
            break
        fi
        diff test.cmp test.out > /dev/null 2>&1
        difference=$?
        if [[ $difference -eq 1 ]]
        then
            echo "Difference found:"
            echo "test.cmp | test.out"
            diff test.cmp test.out
            completed=0
            break
        fi
    done
    rm test
    rm correct
    if [[ $completed -eq 1 ]]
    then
        echo "Completed $ITERATIONS tests successfuly."
        rm test.cmp
        rm test.in
        rm test.out
    fi
}

function checkresult {
    # Checks that test output is valid by running a postprocessing check against it
    # Arguments
        # Test generator -> Outputs a single test case to stdout.
        # Test script
        # Postprocessing -> Python script, takes 2 arguments: test_input, test_output. Outputs GOOD if good, otherwise some error information.
        # Num tests
    clear;clear
    if [[ $2 == *.c* ]];
    then
        compile $2 sol
    fi
    ITERATIONS=${4:-50}
    completed=1
    for (( i=1; i<=ITERATIONS; i++ )) do
        echo "Test #$i"
        python3 $1 > test.in
        if [[ $2 == *.c* ]];
        then
            ./sol < test.in > test.out
        fi
        if [[ $2 == *.py ]];
        then
            python3 $2 < test.in > test.out
        fi
        error=$?
        if [[ $error -ne 0 ]]
        then
            echo "Error on test case with test script"
            completed=0
            break
        fi
        python3 $3 test.in test.out > test.result
        str=GOOD
        if [[ $(< test.result) != "$str" ]]; then
            echo "Post processing failed."
            cat test.result
            completed=0
            break
        fi
    done
    if [[ $completed -eq 1 ]]
    then
        echo "Completed $ITERATIONS tests successfuly."
        rm test.result
        rm test.in
        rm test.out
    fi
}
