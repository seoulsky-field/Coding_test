fun main() {
    var arr = Array(26, {-1})
    var str = readLine()

    if (str != null) {
        for (idx in 0 until str.length) {
            if (arr[str[idx].toInt()-97] == -1) {
                arr[str[idx].toInt()-97] = idx
            }
        }
    }

    for (idx in 0 until arr.size) {
        print("${arr[idx]} ")
    }
}