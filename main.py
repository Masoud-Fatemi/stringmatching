class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            
            haystack = list(haystack)
            # needle = list(needle)

            for i in xrange(len(haystack)):
                if ''.join([s for s in haystack[i:(i+len(needle))]]) == needle:
                    break
            return i
        else:
            return -1