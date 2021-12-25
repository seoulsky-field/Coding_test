fun main() {
    val x = readLine()!!.toInt()
    val y = readLine()!!.toInt()
    var quadrant: Int = 0

    if (x > 0 && y > 0) quadrant = 1
    else if (x < 0 && y > 0) quadrant = 2
    else if (x < 0 && y < 0) quadrant = 3
    else if (x > 0 && y < 0) quadrant = 4

    println(quadrant)
}