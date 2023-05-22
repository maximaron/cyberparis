init 15 python:
    skill_minigame_bar = 90
    skill_minigame_score = 0
    skill_you_press_button = 0
init:
    transform skill_point_move(frp):
        subpixel True
        rotate_pad True
        align(0.5,-0.53)
        rotate frp
screen skill_2_minigame:
    add "minigame/Fable_bar.png" align(0.5, 0.5)
    add "minigame/Fable_point.png" at skill_point_move(skill_minigame_bar)
    text "[skill_minigame_score]\nGoodHit" align(0.5, 0.1)
    text "[skill_minigame_bar]\nBar Value" align(0.5, 0.2)

    if skill_minigame_bar >= -14 and skill_minigame_bar <= 14:
        key "K_SPACE":
            if skill_you_press_button == 0:
                if skill_minigame_score < 4:
                    action [SetVariable("skill_minigame_score", skill_minigame_score + 1), SetVariable("skill_you_press_button", skill_you_press_button + 1), Show("you_press_button_good")]
                else:
                    action Jump("end_minigame")
            elif skill_you_press_button == 1:
                action SetVariable("skill_minigame_score", skill_minigame_score + 0)
    else:
        key "K_SPACE" action [SetVariable("skill_minigame_score", 0), Show("you_press_button_bad")]

screen skill_timer_left:
    timer 0.0009 repeat True action [If(skill_minigame_bar >= -90, SetVariable("skill_minigame_bar", skill_minigame_bar - 1)),If(skill_minigame_bar == -90, Hide("skill_timer_left"), Show("skill_timer_right")), If(skill_minigame_bar == -90, SetVariable("skill_you_press_button", 0))]
screen skill_timer_right:
    timer 0.0009 repeat True action [If(skill_minigame_bar <= 90, SetVariable("skill_minigame_bar", skill_minigame_bar + 1)),If(skill_minigame_bar == 90, Hide("skill_timer_right"), Show("skill_timer_left")), If(skill_minigame_bar == 90, SetVariable("skill_you_press_button", 0))]

screen you_press_button_good:
    text "{color=#1e8e00}Good Work!{/color}" at skill_move_good
    timer 1.0 action Hide("you_press_button_good")
screen you_press_button_bad:
    #hbox at skill_move_bad:
    text "{color=#950000}Ups...\nTry Again.{/color}" at skill_move_bad
    timer 1.0 action Hide("you_press_button_bad")
transform skill_move_good:
    align(0.5,0.5)
    linear 0.05 zoom 1.3
    linear 0.5 zoom 1.0 alpha 0.0
transform skill_move_bad:
    align(0.5,0.5)
    linear 0.04 xalign 0.5
    linear 0.06 xalign 0.495
    linear 0.06 xalign 0.515
    linear 0.06 xalign 0.5
    linear 0.5 alpha 0.0
################################################################################
label start_minigame:
    show screen skill_timer_left
    call screen skill_2_minigame
################################################################################
label end_minigame: #End minigame. And jump continue game
    hide screen skill_2_minigame
    hide screen skill_timer_left
    hide screen skill_timer_right
    $ renpy.pause(0.3)
    jump end #continue game
