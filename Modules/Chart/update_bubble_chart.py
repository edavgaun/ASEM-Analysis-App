@interact(top_words=WS())
def update_bubble_chart(top_words):
    Bubble_chart(*top_words)