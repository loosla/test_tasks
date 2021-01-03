

class ValidateParentheses:
    '''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Example:
    Input: s = "()[]{}"
    Output: true
    Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
    '''
    #"[](){}{}()")
    # "[](()){}{}()"
    # "([)]"
    # "[([]])"

    tmp_list = []

    def isValid(self, s: str) -> bool:
        self.tmp_list = []
        if s:
            for i in s:
                if not self.tmp_list:
                    self.tmp_list.append(i)
                else:
                    if self.can_remove_from_tmp_list(i):
                        self.tmp_list.pop()
                    else:
                        self.tmp_list.append(i)
            if not self.tmp_list:
                return True
        return False

    def can_remove_from_tmp_list (self, ch: str) -> bool:
        if ch == ')':
            if self.tmp_list[-1] == '(':
                return True
        elif ch == '}':
            if self.tmp_list[- 1] == '{':
                return True
        elif ch == ']':
            if self.tmp_list[- 1] == '[':
                return True
        return False
