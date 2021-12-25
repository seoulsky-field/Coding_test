fun main() {
    var num: Int = readLine()!!.toInt()
    var newNum: Int = num
    var count: Int = 0

    do {
        newNum = (newNum % 10) * 10 + (newNum / 10 + newNum % 10) % 10
        count++
    } while (!num.equals(newNum))

    println(count)
}