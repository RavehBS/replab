kill -9 `ps | grep python | head -n1 | awk '{print $1;}'`
