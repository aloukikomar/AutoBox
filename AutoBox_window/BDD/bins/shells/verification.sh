function resultfunc()
{
if [ $1 == 0 ];then
        echo "0"
else
        echo "1"
fi

}


value=1
resultfunc $value


