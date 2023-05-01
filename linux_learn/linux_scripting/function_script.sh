# !/bin/bash

function m1()
{
    echo "call from m1"
}

function m2()
{
    let params_1=${1}
    echo "call from m2 ${1}"
}

# calling
m1
m2 params1
