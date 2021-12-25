fun main() {
    val num: Int = readLine()!!.toInt()

    for (i in 1..num) {
        val star: String = "*".repeat(i)
        println(star)
    }
}