class Solution(object):
    def getHint(self, secret, guess):
        """
        You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend
        to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many
        digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many
         digits match the secret number but locate in the wrong position (called "cows"). Your friend will use
         successive guesses and hints to eventually derive the secret number.

        Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls
        and B to indicate the cows.

        Please note that both secret number and friend's guess may contain duplicate digits.

        Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are
        always equal.

        Runtime: 44 ms, faster than 82.40% of Python3 online submissions for Bulls and Cows.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Bulls and Cows.


        Parameters
        ----------
        secret : str

        guess : str

        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().getHint("1807", "7810")
        "1A3B"

        >>> Solution().getHint("1123", "0111")
        "1A1B"

        """

        bulls = 0
        cows = 0
        mem = {}
        s_set = list(secret)
        g_set = list(guess)
        for idx in range(len(s_set)):
            if s_set[idx] == g_set[idx]:
                bulls += 1
                continue

            # print(Solution().getHint("1123", "0111"))
            try:
                s_c = mem[s_set[idx]] + 1
                if s_c <= 0:
                    cows += 1
                mem[s_set[idx]] = s_c
            except KeyError:
                mem[s_set[idx]] = 1

            try:
                g_c = mem[g_set[idx]] - 1
                if g_c >= 0:
                    cows += 1
                mem[g_set[idx]] = g_c
            except KeyError:
                mem[g_set[idx]] = -1

        return """{}A{}B""".format(str(bulls), str(cows))
