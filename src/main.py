# This is a sample Python script.
import os
import sys
import time
from datetime import datetime

import cv2
import numpy as np
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
from PIL import Image

MATERIAL_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/material_task.png'
GOLDEN_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/goldenfish.png'
COOK_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/cook_task.png'
ELITE_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/elite_task.png'
PYRAMID_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/pyramid_task.png'
WEEKLY_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/weekly_task.png'
UPGRADE_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/upgrade_task.png'
CIYUAN_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/ciyuan_task.png'
JUNTUAN_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/juntuan_task.png'
HUNDUN_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/hundun_task.png'
YUANZHENG_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/yuanzheng.png'
MONSTER_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/monster_task.png'
ELITE_TASK_STEP2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/elite_task_step2.png'
UPGRADE_TASK_STEP2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/upgrade_enter_step2.png'
UPGRADE_TASK_STEP22 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/upgrade_enter_step22.png'

PYRAMID_TASK_TITLE = "/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/pyramid_title.png"
WULIN_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/wulin_task.png'
ENTER_WULIN = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/enter_wulin.png'
ENTER_WULIN2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/enter_wulin2.png'
ENTER_WULIN3 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/enter_wulin3.png'
ENTER_WULIN_STEP0 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/enter_wulin_step0.png'
ENTER_WULIN_STEP2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/enter_wulin_step2.png'
DISABLED_ELITE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/elite_disabled.png'
DISABLED_GOLDEN = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/golden_disabled.png'
DISABLED_PYRAMID = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/pyramid_disabled.png'
MONSTER_TASK_EXPERIENCE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/monster_experience.png'

QUICK_TEAM = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/quick_team.png'

EXPERIENCE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/experience.png'
EXPERIENCE_SELECTED = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/experience_selected.png'
PUDDING = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/pudding.png'
PUDDING2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/pudding2.png'
RECIPE1 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/recipe1.png'
RECIPE2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/recipe2.png'

RECIPE3 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/recipe3.png'

GONGHUI = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/gonghui.png'
GONGHUI_TREE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/gonghui_tree.png'

NO_IMAGE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/no.png'
NO2_IMAGE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/no2.png'
ENTER_IMAGE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/enter.png'
ENTER_IMAGE_JUNTUAN = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/juntuan_enter.png'
YES = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/yes.png'
YES2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/yes2.png'

PLUS_IMAGE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/plus.png'
ZERO_IMAGE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/zero_ticket.png'
EXIT = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/exit.png'
EXIT2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/exit2.png'
LEAVE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/leave.png'
NOT_NOW = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/not_now.png'
BACK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/back.png'
MONSTER_BACK ='/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/monster_back.png'
GROW_UP = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/growup_task.png'
GROW_UP_PAGE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/grow_up_page.png'
RECEIVE_ALL = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/receive_all.png'
RECEIVE_ALL2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/receive_all2.png'
MENU_WEEKLY = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/menu_weekly_task.png'
MENU_LINGZHU = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/menu_lingzhu.png'

PINGKEBING = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/pingkebing.png'
ZHAKUN = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/zhakun.png'
DRAGON = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/dragon.png'
QUEEN = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/queen.png'
COW = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/cow.png'
HUNDUN_PAGE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/hundun_page.png'

KUNNAN = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/difficult.png'
YUANZHENG_PAGE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/yuanzheng_page.png'
JUNTUAN_BACK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/juntuan_back.png'
JUNTUAN_LEAVE2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/juntuan_leave2.png'
SWITCH_ACCOUNT = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/switch_account.png'
SWITCH_BUTTON = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/switch_button.png'

SWITCH_ACCOUNT_ICON = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/switch_account.png'
TASK_ICON = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/task_icon.png'

TASK_RUNNING_PAGE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/in_team.png'
TASK_PAGE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/task_page.png'

SHESHOU = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/sheshou.png'
FASHI = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/fashi.png'
ZHUJIAO = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/zhujiao.png'
CHUANZHANG = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/chuanzhang.png'
ZHANSHEN = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/zhanshen.png'
SHUANGDAO = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/shuangdao.png'

EX1 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/ex1.png'
EX2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/ex2.png'
EX3 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/ex3.png'
EX4 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/ex4.png'
EX5 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/ex5.png'
EX6 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/ex6.png'
CANCEL = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/cancel.png'

menu_x, menu_y = 890, 107
task_x, task_y = 706, 110

bag_x, bag_y = 845, 107
daily_task_x, daily_task_y = 820, 290
# Capture the specific area of the screen
x, y, width, height = 0, 70 * 2, 950 * 2, 600 * 2


def get_current_day():
    # Get the current date
    current_date = datetime.today()

    # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    day_of_week = (current_date.weekday() + 1) % 7

    # Convert the number to the name of the day
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day = days[day_of_week]
    print(current_day)
    return current_day


def find_image_on_screen(image_path, confidence=0.86, attempts=3, region=(x, y, width, height)):
    count = 0
    file_name = os.path.basename(image_path)
    start = time.time()
    while count < attempts:
        try:

            screenshot = pyautogui.screenshot()
            # screenshot.save("./screenshot.png")
            # Load the image to be found
            image_to_find = Image.open(image_path)
        except:
            print("pic file not able to open", file_name)
            return None
        # Take a screenshot of the entire screen

        try:
            location = pyautogui.locate(image_to_find, screenshot, region=region,
                                        confidence=confidence)
            res_x, res_y = location.left / 2.0 + location.width / 4, location.top / 2.0 + location.height / 4
            pyautogui.moveTo(res_x, res_y)
            return res_x, res_y
        except:
            count += 1
            continue
    # Search for the image within the screenshot

  #  print(f"{file_name} not found. cost time: ", time.time() - start)
    return None


def get_file_name(file_path):
    return os.path.basename(file_path)


def click_image(image_path, attempts=2, confidence=0.82, clicks=1, x_offset=0, y_offset=0,
                region=(x, y, width, height)):
    result = find_image_on_screen(image_path, confidence=confidence, attempts=attempts, region=region)
    if result is not None:
        # Click on the center of the found image
        pyautogui.moveTo(result[0] + x_offset, result[1] + y_offset, duration=0.2)
        click(result[0] + x_offset, result[1] + y_offset, clicks=clicks, interval=0.2)
        print("Clicked on the image", get_file_name(image_path))
        return True
    else:
        print(" Error: Unable to find image ", get_file_name(image_path))


def drag_to_left():
    current_position = daily_task_x, daily_task_y
    pyautogui.moveTo(x=daily_task_x, y=daily_task_y, duration=0.1)
    # Calculate the destination position to the left (assuming a drag distance)
    destination_position = ((current_position[0] - 600), current_position[1])

    # Drag the mouse cursor to the left
    pyautogui.dragTo(x=destination_position[0], y=destination_position[1], button='left', duration=0.9)
    pyautogui.mouseUp(button='left')


def test():
    offset = 100
    pyautogui.keyDown('shift')
    pyautogui.scroll(offset)
    pyautogui.keyUp('shift')


def go_home():
    pyautogui.press('esc')
    time.sleep(0.2)
    if click_image(CHECK, attempts=1):
        click_image(YES)
    pyautogui.press('esc')
    if click_image(CHECK, attempts=1):
        click_image(YES)
    pyautogui.press('esc')
    pyautogui.press('esc')
    pyautogui.press('esc')
    if click_image(NO_IMAGE) or click_image(NO2_IMAGE, attempts=1):
        time.sleep(0.5)


def click(x=None, y=None, clicks=1, interval=0.0, duration=0.0):
    pyautogui.click(x=x, y=y, clicks=clicks, interval=interval, duration=duration)
    time.sleep(0.2)


def click_game_frame():
    game_frame_x, game_frame_y = 175, 450
    click(game_frame_x, game_frame_y)


def go_task_page():
    if find_image_on_screen(TASK_PAGE, attempts=1):
        return
    go_home()
    click(task_x, task_y)
    if not find_image_on_screen(TASK_PAGE):
        print("unable to find task page, retry")
        click_game_frame()
        go_home()
        click(task_x, task_y)


def start_material_task():
    print("start material task")
    if not click_image(MATERIAL_TASK):
        print("failed to enter material")
        return False
    if not click_image(ENTER_IMAGE, clicks=2):
        print("no ticket")
        pyautogui.press("esc")
        time.sleep(0.5)
        return True
    # click_image(PLUS_IMAGE, clicks=4)
    click_image(YES, clicks=2)
    time.sleep(1)
    click_image(YES, clicks=2)
    time.sleep(10)
    if find_image_on_screen(YES) or find_image_on_screen(ENTER_IMAGE) or find_image_on_screen(MATERIAL_TASK):
        print("failed to enter material task")
        pyautogui.press("esc")
        time.sleep(0.5)
        return True
    wait_for_finish(total_time=295)
    # wait
    return True


def start_golden_fish():
    print("start golden fish task")
    click_image(GOLDEN_TASK)
    if find_image_on_screen(DISABLED_GOLDEN):
        print("task disabled, no ticket")
        pyautogui.press("esc")
        time.sleep(0.5)
        return True
    click_image(QUICK_TEAM)
    # click_image(PLUS_IMAGE, clicks=3)
    click_image(YES)
    time.sleep(4)
    if find_image_on_screen(GOLDEN_TASK) or find_image_on_screen(DISABLED_GOLDEN) or find_image_on_screen(
            QUICK_TEAM) or find_image_on_screen(PLUS_IMAGE):
        print("failed to enter task")
        pyautogui.press("esc")
        time.sleep(0.5)
        return False
    wait_for_finish(200)
    return True


def start_cook_task():
    print("start cook task")
    click_image(COOK_TASK)
    click_image(PUDDING)
    if find_image_on_screen(PUDDING):
        print("retry")
        click_image(PUDDING2)
    click_image(ENTER_IMAGE)
    if not click_image(RECIPE1, y_offset=-50, confidence=0.8)\
            or not click_image(RECIPE2, y_offset=-50,confidence=0.8) \
            or not click_image(RECIPE3, y_offset=-50, confidence=0.8):
        print("No ticket")
        pyautogui.press("esc")
        time.sleep(0.5)
        return True
    click_image(ENTER_IMAGE)
    time.sleep(5)
    if find_image_on_screen(RECIPE1) or find_image_on_screen(ENTER_IMAGE):
        print("failed to enter task")
        go_home()
        return False

    wait_for_finish(100)
    return True


def start_pyramid_task():
    print("start pyramid task")
    click_image(PYRAMID_TASK)
    if find_image_on_screen(DISABLED_PYRAMID):
        print("task disabled, no ticket")
        pyautogui.press("esc")
        time.sleep(0.5)
        return True
    click_image(QUICK_TEAM)
    click_image(PLUS_IMAGE, clicks=7)
    click_image(YES)
    time.sleep(5)
    if find_image_on_screen(PYRAMID_TASK_TITLE) or find_image_on_screen(QUICK_TEAM) or find_image_on_screen(
            PLUS_IMAGE) or find_image_on_screen(
        YES) or find_image_on_screen(PYRAMID_TASK):
        print("failed to enter task")
        go_home()
        return False
    wait_for_finish()
    return True


def start_elite_task():
    print("start elite task")
    click_image(ELITE_TASK)
    if find_image_on_screen(DISABLED_ELITE):
        print("task disabled, no ticket")
        pyautogui.press("esc")
        time.sleep(0.5)
        return True
    # click_image(ELITE_TASK_STEP2, clicks=3, x_offset=-50)
    click_image(QUICK_TEAM)
    click_image(PLUS_IMAGE, clicks=3)
    click_image(YES)
    time.sleep(5)
    if find_image_on_screen(QUICK_TEAM) or find_image_on_screen(PLUS_IMAGE) or find_image_on_screen(
            YES) or find_image_on_screen(ELITE_TASK) or find_image_on_screen(DISABLED_ELITE):
        print("failed to enter task")
        go_home()
        return False
    wait_for_finish(total_time=350)
    return True


def start_weekly_task():
    print("start weekly task")
    if not click_image(WEEKLY_TASK, confidence=0.8):
        return False
    if not find_image_on_screen(ENTER_IMAGE):
        print("ERROR: NO ticket found")
        pyautogui.press("esc")
        time.sleep(0.5)
        return True
    click_image(ENTER_IMAGE, clicks=2)
    click_image(PLUS_IMAGE, clicks=7)
    click_image(YES, clicks=2)

    time.sleep(10)
    if find_image_on_screen(YES, attempts=1) or find_image_on_screen(
            ENTER_IMAGE, attempts=1) or find_image_on_screen(WEEKLY_TASK, attempts=1):
        print("failed to enter weekly task")
        go_home()
        return True
    wait_for_finish(140)
    return True


def start_upgrade_task():
    print("start upgrade task")
    click_image(UPGRADE_TASK)
    if not find_image_on_screen(EXPERIENCE_SELECTED, confidence=0.95):
        print("experience not selected")
        click_image(EXPERIENCE, confidence=0.95)

    click_image(ENTER_IMAGE)
    time.sleep(0.2)
    if not find_image_on_screen(PLUS_IMAGE):
        print("no ticket")
        pyautogui.press("esc")
        go_task_page()
        return True
    click_image(PLUS_IMAGE, clicks=5)
    click_image(YES, clicks=1)
    time.sleep(1)
    if find_image_on_screen(PLUS_IMAGE) or find_image_on_screen(YES):
        print("no ticket")
        pyautogui.press("esc")
        go_task_page()
        return True

    if click_image(UPGRADE_TASK_STEP2, confidence=0.9, clicks=1) or click_image(UPGRADE_TASK_STEP22, confidence=0.92,
                                                                                clicks=1):
        time.sleep(10)

    if find_image_on_screen(YES, attempts=1) or find_image_on_screen(
            EXPERIENCE) or find_image_on_screen(ENTER_IMAGE, attempts=1) or find_image_on_screen(
        UPGRADE_TASK, attempts=1) or find_image_on_screen(UPGRADE_TASK_STEP2, attempts=1):
        print("failed to enter task")
        go_home()
        return False
    wait_for_finish(400)
    return True


def start_ciyuan_task():
    print("ciyuan")
    if not click_image(CIYUAN_TASK):
        print("Failed enter ciyuan")
        return False
    if not find_image_on_screen(QUICK_TEAM):
        print("no ticket found")
        pyautogui.press("esc")
        time.sleep(0.5)
        return True
    click_image(QUICK_TEAM)
    click_image(PLUS_IMAGE, clicks=5)
    click_image(YES)
    time.sleep(10)
    if find_image_on_screen(QUICK_TEAM) or find_image_on_screen(PLUS_IMAGE) or find_image_on_screen(YES):
        print("failed to enter task ciyuan")
        return False
    wait_for_finish(350)
    return True


MONSTER_ENTER = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/monster_enter.png'


def start_monster_task():
    print("monster task")
    if not click_image(MONSTER_TASK):
        print("failed to enter monster task icon")
        return False
    if not click_image(ENTER_IMAGE):
        print("no ticket")
        pyautogui.press("esc")
        time.sleep(0.5)
        return True
    # click_image(PLUS_IMAGE, clicks=2)
    click_image(YES)
    click_image(MONSTER_TASK_EXPERIENCE)
    time.sleep(0.4)
    click(x=563, y=539)
    time.sleep(5)
    if find_image_on_screen(MONSTER_TASK) or find_image_on_screen(ENTER_IMAGE) or find_image_on_screen(PLUS_IMAGE):
        print("ENTER failed")
        pyautogui.press("esc")
        time.sleep(0.5)
        return False
    wait_for_finish(total_time=300)
    return True


def start_wulin_task():
    print("wulin task")
    # return True
    if not click_image(WULIN_TASK):
        print("failed to enter wulin icon")
        return False
    click_image(ENTER_WULIN_STEP0)
    time.sleep(1)
    click_image(YES, clicks=4)
    if not find_image_on_screen(ENTER_WULIN) and not find_image_on_screen(ENTER_WULIN2):
        print("no ticket found")
        pyautogui.press("esc")
        time.sleep(0.5)
        return False
    if click_image(ENTER_WULIN) or click_image(ENTER_WULIN3) or click_image(ENTER_WULIN2):
        click_image(ENTER_WULIN_STEP2)
        time.sleep(5)
    if find_image_on_screen(ENTER_WULIN, attempts=1) or find_image_on_screen(ENTER_WULIN_STEP2,
                                                                             attempts=1) or find_image_on_screen(
        WULIN_TASK, attempts=1):
        print("failed to enter wulin task")
        return False
    wait_for_finish(300)
    return True


def wait_for_finish(total_time=300):
    print("wait for finish")
    start = time.time()
    interval = 3
    while time.time() - start < total_time:

        if click_image(BACK) or click_image(EXIT) or click_image(LEAVE) or click_image(EXIT2) or click_image(MONSTER_BACK):
            cost = time.time() - start
            print("Task finished, cost : ", cost)
            time.sleep(2)
            pyautogui.press("esc")
            time.sleep(0.5)
            return True
            # go_home()
        time.sleep(interval)


    print("After waited max time, still not found EXIT button")
    return False


def start_hundun_task1(type=ZHAKUN, total_time=200):
    print("start hundun,", get_file_name(type))

    time.sleep(1)
    if not find_image_on_screen(TASK_RUNNING_PAGE) and not find_image_on_screen(type):
        print("no ticket for task", get_file_name(type))
        return True
    click_image(type)
    click_image(QUICK_TEAM)
    start = time.time()
    while time.time() - start < 50:
        time.sleep(5)
        if find_image_on_screen(TASK_RUNNING_PAGE):
            print("found task running")
            break
    if not find_image_on_screen(TASK_RUNNING_PAGE):
        print("still not found team pic")
        juntuan_go_home()
        go_home()
        return False
    if find_image_on_screen(HUNDUN_PAGE, attempts=1) or find_image_on_screen(HUNDUN_TASK, attempts=1):
        print("failed to enter hundun")
        go_home()
        return False
    finished = shoot(total_time=total_time, team=True)
    if finished:
        walk_around()
        juntuan_go_home()
        return True
    juntuan_go_home()
    return False


def start_hundun_task3():
    print("start hundun 3")
    click_image(HUNDUN_TASK)
    if not find_image_on_screen(PINGKEBING):
        print("no ticket for hundun 3")
        return True
    click_image(PINGKEBING, clicks=2)
    click_image(QUICK_TEAM, clicks=2)
    time.sleep(5)
    if find_image_on_screen(HUNDUN_PAGE, attempts=1) or find_image_on_screen(HUNDUN_TASK, attempts=1):
        print("failed to enter hundun3")
        go_home()
        return False
    finished = shoot(total_time=300)
    if finished:
        walk_around()
        juntuan_go_home()
        return True

    juntuan_go_home()
    return False


def start_juntuan_task1():
    print("start juntuan 1")
    click_image(JUNTUAN_TASK)
    if not find_image_on_screen(ENTER_IMAGE) and not find_image_on_screen(ENTER_IMAGE_JUNTUAN):
        print("no ticket for juntuan 1")
        return True
    click_image(ENTER_IMAGE)
    click_image(ENTER_IMAGE_JUNTUAN)
    time.sleep(5)
    if find_image_on_screen(ENTER_IMAGE) or find_image_on_screen(JUNTUAN_TASK):
        print("failed to enter juntuan")
        go_home()
        return False
    finished = shoot(total_time=370)
    if finished:
        walk_around()
        juntuan_go_home()
        print("finished")
        return True
    else:
        juntuan_go_home()
        return False


def juntuan_go_home():
    pyautogui.press('esc')
    time.sleep(0.2)
    pyautogui.press('esc')
    pyautogui.press('esc')
    time.sleep(0.5)
    if not find_image_on_screen(BACK) and not find_image_on_screen(JUNTUAN_BACK):
        pyautogui.press('esc')
        time.sleep(1)
    print(" juntuan back")
    if click_image(JUNTUAN_BACK, clicks=1) or click_image(JUNTUAN_LEAVE2, clicks=1):
        time.sleep(1)
        return
    pyautogui.press('esc')
    time.sleep(0.5)
    if click_image(JUNTUAN_BACK, clicks=1) or click_image(JUNTUAN_LEAVE2, clicks=1):
        time.sleep(1)
        return


def shoot(total_time=350, team=False):
    # click_game_frame()
    finished = False
    time.sleep(15)
    start = time.time()
    click_game_frame()
    while time.time() - start < total_time:
        print("repeate shoot")
        # pyautogui.press("g", presses=4, interval=0.3)
        pyautogui.press("c", presses=4, interval=0.3)
        # pyautogui.press("e", presses=3, interval=0.5)
        pyautogui.press("r", presses=4, interval=0.3)
        pyautogui.press("v", presses=4, interval=0.3)
        pyautogui.press("x", presses=1)
        pyautogui.press("g", presses=40, interval=0.3)

        click_game_frame()
        if team and not find_image_on_screen(TASK_RUNNING_PAGE):
            if find_image_on_screen(YES, attempts=1):
                click_image(YES)
                finished = True
                break
            else:
                print("stop shoot, teammates gone")
                return False
        if find_image_on_screen(YES, attempts=1):
            click_image(YES)
            finished = True
            break
        if find_image_on_screen(LEAVE, attempts=1):
            click_image(LEAVE)
            print("failed finish")
            return False
        if finished:
            break
    cost = time.time() - start
    print("Task finished,juntuan cost : ", cost)
    if finished:
        return True
    print("timed out, still not finished")
    return False


def receive_daily_award():
    go_home()
    click(menu_x, menu_y)

    click_image(GROW_UP)
    if not find_image_on_screen(GROW_UP_PAGE, attempts=1):
        print("failed to enter grow up page, retry")
        go_home()
        time.sleep(1)
        click(menu_x, menu_y)
        click_image(GROW_UP)
        if not find_image_on_screen(GROW_UP_PAGE):
            print("failed to enter grow up page")
            return False
    receive_all_award()
    click_image(MENU_WEEKLY)
    receive_all_award()
    click_image(MENU_LINGZHU)
    receive_all_award()


def receive_all_award():
    receive_one_award()
    receive_one_award()
    receive_one_award()


def receive_one_award():
    if click_image(RECEIVE_ALL, clicks=1) or click_image(RECEIVE_ALL2):
        if click_image(YES, clicks=1) or click_image(YES2, clicks=1, attempts=1):
            return


def walk_around():
    walk_right(7)


def walk_left(seconds):
    time.sleep(1)
    start = time.time()
    print("left move")
    while time.time() - start < seconds:  # Hold Key for 5 Seconds
        pyautogui.keyDown('left')
    pyautogui.keyUp('left')


def walk_right(seconds):
    time.sleep(1)
    start = time.time()
    print("right move")
    while time.time() - start < seconds:  # Hold Key for 8 Seconds
        pyautogui.keyDown('right')
    pyautogui.keyUp('right')
    time.sleep(1)


def start_gonghui():
    go_home()
    click(menu_x, menu_y)
    click_image(GONGHUI)
    time.sleep(2)
    click_image(GONGHUI_TREE)
    click_image(YES)
    pyautogui.press("esc")
    pyautogui.press("esc")


def get_mouse_location():
    current_mouse_position = pyautogui.position()
    # Print the current mouse position
    print("Current mouse position:", current_mouse_position)


def start_daily_tasks():
    count = 0
    finished_task = []
    go_task_page()
    while count < 12 and len(finished_task) < 10:
        drag_count = 0
        go_task_page()
        count += 1
        if get_file_name(MONSTER_TASK) not in finished_task:
            if test_task_start_monster_task():
                finished_task.append(get_file_name(MONSTER_TASK))
                count += 1
            print("finished handle task: ", get_file_name(MONSTER_TASK))
            go_task_page()
        while drag_count < 2:
            print("looking for task, attempt ", count)
            found = False
            print("task added into finished list ", finished_task)

            if get_file_name(PYRAMID_TASK) not in finished_task and find_image_on_screen(PYRAMID_TASK, attempts=3):
                if start_pyramid_task():
                    finished_task.append(get_file_name(PYRAMID_TASK))
                    count += 1
                #    found = True
                print("finished handle task: ", get_file_name(PYRAMID_TASK))
                #  break
                go_task_page()
            if get_file_name(ELITE_TASK) not in finished_task and find_image_on_screen(ELITE_TASK, attempts=1):
                if start_elite_task():
                    finished_task.append(get_file_name(ELITE_TASK))
                    count += 1
                #   found = True
                print("finished handle task: ", get_file_name(ELITE_TASK))
                # break
                go_task_page()
            if get_file_name(MATERIAL_TASK) not in finished_task and find_image_on_screen(MATERIAL_TASK, attempts=1):
                if start_material_task():
                    finished_task.append(get_file_name(MATERIAL_TASK))
                    count += 1
                # found = True
                print("finished handle task: ", get_file_name(MATERIAL_TASK))
                # break
                go_task_page()

            if get_file_name(GOLDEN_TASK) not in finished_task and find_image_on_screen(GOLDEN_TASK, attempts=1):
                if start_golden_fish():
                    finished_task.append(get_file_name(GOLDEN_TASK))

                    count += 1
                #   found = True
                print("finished handle task: ", get_file_name(GOLDEN_TASK))
                # break
                go_task_page()

            print("here")
            if get_file_name(WEEKLY_TASK) not in finished_task and find_image_on_screen(WEEKLY_TASK, confidence=0.82,
                                                                                        attempts=1):
                print("check")
                if start_weekly_task():
                    finished_task.append(get_file_name(WEEKLY_TASK))
                    count += 1
                #    found = True
                print("finished handle task: ", get_file_name(WEEKLY_TASK))
                # break
                go_task_page()

            if get_file_name(WULIN_TASK) not in finished_task and find_image_on_screen(WULIN_TASK, attempts=1):
                if start_wulin_task():
                    finished_task.append(get_file_name(WULIN_TASK))
                    count += 1
                #     found = True
                print("finished handle task: ", get_file_name(WULIN_TASK))
                # break
                go_task_page()

      #      if get_file_name(CIYUAN_TASK) not in finished_task and find_image_on_screen(CIYUAN_TASK, attempts=1):
       #         if start_ciyuan_task():
        #            finished_task.append(get_file_name(CIYUAN_TASK))
         #           count += 1
                #     found = True
          #      print("finished handle task: ", get_file_name(CIYUAN_TASK))
                # break
           #     go_task_page()

            if get_file_name(JUNTUAN_TASK) not in finished_task and find_image_on_screen(JUNTUAN_TASK, attempts=1):
                if start_juntuan_task1():
                    finished_task.append(get_file_name(JUNTUAN_TASK))
                    count += 1
                go_task_page()
                #     found = True
                print("finished handle task: ", get_file_name(JUNTUAN_TASK))
            drag_count += 1
            drag_to_left()
        go_home()

        #  break


def test_task_start_material_task():
    go_task_page()
    count = 0
    while not find_image_on_screen(MATERIAL_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if find_image_on_screen(MATERIAL_TASK):
        start_material_task()


def test_task_start_monster_task():
    go_task_page()
    count = 0
    while not find_image_on_screen(MONSTER_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if find_image_on_screen(MONSTER_TASK):
        return start_monster_task()
    return False


def test_task_start_golden_fish():
    go_task_page()
    count = 0
    while not find_image_on_screen(GOLDEN_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if find_image_on_screen(GOLDEN_TASK):
        start_golden_fish()


def test_task_start_pyramid_task():
    go_task_page()
    count = 0
    while not find_image_on_screen(PYRAMID_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if find_image_on_screen(PYRAMID_TASK):
        start_pyramid_task()


def test_task_start_upgrade_task():
    go_task_page()
    count = 0
    while not find_image_on_screen(UPGRADE_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if find_image_on_screen(UPGRADE_TASK):
        start_upgrade_task()


def test_task_start_weekly_task():
    go_task_page()
    count = 0
    while not find_image_on_screen(WEEKLY_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if find_image_on_screen(WEEKLY_TASK):
        start_weekly_task()


def test_task_start_ciyuan_task():
    go_task_page()
    count = 0
    while not find_image_on_screen(CIYUAN_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if find_image_on_screen(CIYUAN_TASK):
        start_ciyuan_task()


def test_task_start_wulin_task():
    go_task_page()
    count = 0
    while not find_image_on_screen(WULIN_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if find_image_on_screen(WULIN_TASK):
        start_wulin_task()


def test_task_start_elite_task():
    go_task_page()
    count = 0
    while not find_image_on_screen(ELITE_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if find_image_on_screen(ELITE_TASK):
        start_elite_task()


def test_task_start_cook_task():
    go_task_page()
    count = 0
    while not find_image_on_screen(COOK_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if find_image_on_screen(COOK_TASK):
        start_cook_task()


def test_task_start_juntuan_task1():
    go_task_page()
    count = 0
    while not find_image_on_screen(JUNTUAN_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if find_image_on_screen(JUNTUAN_TASK):
        start_juntuan_task1()


def switch_Account(account):
    go_home()
    click(x=menu_x, y=menu_y)
    time.sleep(0.5)
    click_image(SWITCH_ACCOUNT)
    click_image(account)
    if not click_image(SWITCH_BUTTON, confidence=0.92, clicks=2):
        print("unable to switch to ", get_file_name(account))
        return False
    time.sleep(5)
    go_home()
    return True


def test_walk():
    time.sleep(2)
    walk_around()


def test_shoot():
    shoot(total_time=20)


def start_all(accounts):
    click_game_frame()
    pet_task()
    for each in accounts:
        print("switch to account " + get_file_name(each))
        if not switch_Account(each):
            print("retry switch account " + each)
            switch_Account(each)
        add_time()
        receive_mails()

        # use_item_before()
        start_gonghui()

        start_daily_tasks()
        receive_mails()
        upgrade_weapon()
        #use_all_items()
        receive_daily_award()


def start_all_hundun(accounts):
    click_game_frame()
    for each in accounts:
        print("Hundunswitch to account " + get_file_name(each))
        switch_Account(each)

        today = get_current_day()
        if today == 'Monday' or today == 'Wednesday' or today == 'Sunday':
            start_hundun_all_tasks(ZHAKUN)
            start_hundun_all_tasks(ZHAKUN)
            start_hundun_all_tasks(ZHAKUN)
        if today == 'Tuesday' or today == 'Thursday' or today == 'Sunday':
            start_hundun_all_tasks(DRAGON)
            start_hundun_all_tasks(DRAGON)
            start_hundun_all_tasks(DRAGON)
        if today == 'Friday' or today == 'Wednesday' or today == 'Sunday':
            start_hundun_all_tasks(PINGKEBING)
            start_hundun_all_tasks(PINGKEBING)
            start_hundun_all_tasks(PINGKEBING)
            start_hundun_all_tasks(PINGKEBING)
        if today == 'Friday' or today == 'Tuesday' or today == 'Sunday':
            start_hundun_all_tasks(QUEEN)
            start_hundun_all_tasks(QUEEN)
            start_hundun_all_tasks(QUEEN)
            start_hundun_all_tasks(QUEEN)
            start_hundun_all_tasks(QUEEN)
        if today == 'Monday' or today == 'Wednesday' or today == 'Sunday':
            # start_hundun_all_tasks(COW)
            ##start_hundun_all_tasks(COW)
            # start_hundun_all_tasks(COW)
            # start_hundun_all_tasks(COW)
            print("cow")

        juntuan_go_home()
        go_home()
        receive_daily_award()


def start_hundun_all_tasks(type=ZHAKUN, total_time=250):
    if find_image_on_screen(TASK_RUNNING_PAGE):
        start_hundun_task1(type, total_time)
        return
    if click_image(HUNDUN_TASK):
        start_hundun_task1(type, total_time)
        return
    if find_image_on_screen(HUNDUN_PAGE):
        start_hundun_task1(type, total_time)
        return
    go_task_page()
    count = 0
    while not find_image_on_screen(HUNDUN_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if click_image(HUNDUN_TASK):
        start_hundun_task1(type)


def start_yuanzheng_task(total_time=180, task_type=ZHAKUN):
    print("start_yuanzheng_task1", get_file_name(task_type))
    if not find_image_on_screen(task_type):
        print("no ticket for yuanzheng ", get_file_name(task_type))
        return True
    click_image(task_type, clicks=2)
    click_image(KUNNAN, clicks=2)
    click_image(QUICK_TEAM, clicks=2)
    time.sleep(2)
    if find_image_on_screen(YUANZHENG_PAGE, attempts=1) or find_image_on_screen(YUANZHENG_TASK, attempts=1):
        print("failed to enter yuanzheng", get_file_name(task_type))
        go_home()
        return False
    print("entered yuanzheng task")
    click_game_frame()
    start = time.time()
    while time.time() - start < 35:
        time.sleep(5)
        if find_image_on_screen(TASK_RUNNING_PAGE):
            print("found task running")
            break
    if not find_image_on_screen(TASK_RUNNING_PAGE):
        print("still not found team pic")
        # juntuan_go_home()
        # go_home()
        return False
    start = time.time()
    finished = False
    print("shooting")
    retry =0
    while time.time() - start < total_time:
        click_game_frame()

        pyautogui.press("v", presses=3, interval=0.5)
        pyautogui.press("c", presses=3, interval=0.5)
        pyautogui.press("r", presses=3, interval=0.5)
        pyautogui.press("x")
        # pyautogui.press("f", presses=3, interval=0.5)
        #  pyautogui.press("d", presses=3, interval=0.5)
        print(" press d")
        pyautogui.press("g", presses=20, interval=0.3)
        if click_image(YES, attempts=1) or click_image(YES2, attempts=1):
            print("found YEs")
            click_image(YES)
            time.sleep(1)
            finished = True
            break
        if not find_image_on_screen(TASK_RUNNING_PAGE) and not find_image_on_screen(YES):
            if click_image(YES, attempts=1) or click_image(YES2, attempts=1):
                print("found YEs")
                click_image(YES)
                time.sleep(1)
                finished = True
                break
            if not find_image_on_screen(TASK_RUNNING_PAGE, confidence=0.8):
                if retry == 2:
                    print("Failed to finish yuanzheng")
                    juntuan_go_home()
                    return False
                else:
                    retry+=1


    if finished:
        walk_right(4)
    juntuan_go_home()
    print("yuanzheng finished")
    return False


def start_all_yuanzheng(accounts):
    start = time.time()
    while time.time() - start < 60 * 60 * 1:
        current_time = datetime.now().time()
        if current_time.hour < 20:
            print("Too far to 9 PM")
            start_all(accounts)
            return
        if current_time.hour == 21:  # 21 represents 9 PM in 24-hour format
            print("It's 9 PM now!")
            break
        click_game_frame()
        print("wait 1 more min")
        time.sleep(60)

    click_game_frame()
    for each in accounts:
        print("switch to account " + get_file_name(each))
        switch_Account(each)
        go_home()
        click_game_frame()
        today = get_current_day()
        if today == 'Monday' or today == 'Wednesday' or today == 'Sunday' or today == 'Saturday':
            go_to_yuanzheng_task(total_time=120, task_type=ZHAKUN)
            go_to_yuanzheng_task(total_time=120, task_type=ZHAKUN)
            go_to_yuanzheng_task(total_time=120, task_type=ZHAKUN)
        if today == 'Monday' or today == 'Wednesday':
            go_to_yuanzheng_task(total_time=220, task_type=COW)
            go_to_yuanzheng_task(total_time=220, task_type=COW)
            go_to_yuanzheng_task(total_time=220, task_type=COW)
            go_to_yuanzheng_task(total_time=220, task_type=COW)
            go_to_yuanzheng_task(total_time=220, task_type=COW)
            go_to_yuanzheng_task(total_time=220, task_type=COW)
            go_to_yuanzheng_task(total_time=220, task_type=COW)
            go_to_yuanzheng_task(total_time=220, task_type=COW)
            go_to_yuanzheng_task(total_time=220, task_type=COW)
        if today == 'Tuesday' or today == 'Thursday' or today == 'Sunday' or today == 'Saturday':
            go_to_yuanzheng_task(total_time=120, task_type=DRAGON)
            go_to_yuanzheng_task(total_time=120, task_type=DRAGON)
            go_to_yuanzheng_task(total_time=120, task_type=DRAGON)
        if today == 'Friday' or today == 'Wednesday' or today == 'Sunday' or today == 'Saturday':
            go_to_yuanzheng_task(total_time=150, task_type=PINGKEBING)
            go_to_yuanzheng_task(total_time=150, task_type=PINGKEBING)
            go_to_yuanzheng_task(total_time=150, task_type=PINGKEBING)
        if today == 'Friday' or today == 'Tuesday' or today == 'Sunday' or today == 'Saturday':
            go_to_yuanzheng_task(total_time=200, task_type=QUEEN)
            go_to_yuanzheng_task(total_time=200, task_type=QUEEN)
            go_to_yuanzheng_task(total_time=200, task_type=QUEEN)


def go_to_yuanzheng_task(total_time=120, task_type=ZHAKUN):
    if find_image_on_screen(YUANZHENG_PAGE):
        print("find yuanzheng page, start")
        start_yuanzheng_task(total_time, task_type)
        return
    go_task_page()
    count = 0
    while not find_image_on_screen(YUANZHENG_TASK, attempts=1) and count < 4:
        count += 1
        drag_to_left()
    if click_image(YUANZHENG_TASK):
        start_yuanzheng_task(total_time=total_time, task_type=task_type)


def test_shoot(total=340):
    click_game_frame()
    shoot(total)


def use_coupon():
    start = time.time()
    while time.time() - start < 60 * 60 * 10:
        click_all_coupon()
        time.sleep(4 * 60)


def click_all_coupon():
    click_image(EX1, confidence=0.9)
    click_image(CANCEL)
    click_image(EX2, confidence=0.9)
    click_image(CANCEL)
    click_image(EX3, confidence=0.9)
    click_image(CANCEL)
    click_image(EX4, confidence=0.93)
    click_image(CANCEL)
    click_image(EX5, confidence=0.9)
    click_image(CANCEL)
    click_image(EX6, confidence=0.9)
    click_image(CANCEL)


WEAPON_UPGRADE_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/weapon_upgrade_task.png'
WEAPON_UPGRADE_PAGE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/weapon_page.png'
WEAPON_1 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/weapon_1.png'

UPGRADE_BUTTON = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/weapon_button.png'


def upgrade_weapon():
    go_home()
    click(menu_x, menu_y)
    time.sleep(0.5)
    click(x=700, y=293)
    click_image(WEAPON_UPGRADE_TASK)
    if not find_image_on_screen(WEAPON_UPGRADE_PAGE):
        print("didnt find weapon upgrade page")
        return False
    if not click_image(WEAPON_1, confidence=0.93):
        print("No weapon upgrade 1 found")
        return True
    # click_image(WEAPON_1, 0.96)
    time.sleep(0.5)
    click_image(UPGRADE_BUTTON)
    time.sleep(3)
    click_image(YES)
    click_image(YES2)
    pyautogui.press('esc')
    pyautogui.press('esc')


PET_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/pet_task.png'
OIL_UP = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/oil_up.png'


def pet_task():
    go_home()
    click(menu_x, menu_y)
    click_image(PET_TASK)
    click_image(OIL_UP)
    pyautogui.press('esc')
    pyautogui.press('esc')


ITEM1 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/item1.png'
ITEM2 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/item2.png'
ITEM3 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/item3.png'
ITEM4 = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/item4.png'
TICKET = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/ticket.png'
USE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/use.png'
MAX = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/max.png'
BAG_USE = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/bag_use.png'

MAIL = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/mail.png'
PERSONAL_MAIL = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/personal_mail.png'
CHECK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/check.png'
RECEIVE_MAIL = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/receive_all_mails.png'
YES_MAIL = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/yes_email.png'


def receive_mails():
    go_home()
    click(menu_x, menu_y)
    time.sleep(0.5)
    click_image(MAIL)
    if click_image(CHECK):
        print("found checkbox")
        pyautogui.press('esc')
    click_image(PERSONAL_MAIL)
    if click_image(RECEIVE_MAIL, confidence=0.9):
        click_image(YES)
    pyautogui.press('esc')
    pyautogui.press('esc')
    pyautogui.press('esc')


def use_all_items():
    go_home()
    click(bag_x, bag_y)
    time.sleep(0.5)

    click_image(BAG_USE)
    use_item(ITEM1)
    use_item(ITEM2)
    use_item(ITEM3)
    use_item(ITEM4)


def use_item(item_image):
    if click_image(item_image):
        click_image(USE)
        time.sleep(3)
        time.sleep(0.5)
        click_image(MAX, clicks=3)
        click_image(YES)
        time.sleep(3)
        click_image(YES)


def use_item_before():
    go_home()
    click(bag_x, bag_y)
    time.sleep(0.5)
    if find_image_on_screen(YES, attempts=2):
        click_image(CHECK)
        print("found checkbox")
        click_image(YES)
    click_image(BAG_USE)
    if click_image(TICKET):
        click_image(USE)
        click_image(CHECK)
        click_image(MAX)
        click_image(USE)
        time.sleep(2)
        pyautogui.press("esc")
    if find_image_on_screen(YES, attempts=2):
        click_image(CHECK)
        print("found checkbox")
        click_image(YES)
    else:
        pyautogui.press("esc")
        if click_image(CHECK):
            click_image(YES)


main_task_x, main_task_y = 162, 342
RECEIVE_AWARD = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/receive_award.png'
NEXT_NEXT = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/next_next.png'
ACCEPT_TASK = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/accept.png'
IS_AUTO_RUNNING = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/is_auto_running.png'
FINISH = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/finish.png'

yes_x, yes_y = 786, 365


def auto_run_task(total_time=60 * 30):
    start = time.time()
    while time.time() - start < total_time:
        if not find_image_on_screen(IS_AUTO_RUNNING):
            time.sleep(2)
            if not find_image_on_screen(IS_AUTO_RUNNING):
                # click_image(TASK_ICON, region=(0, 0, 400, 400))
                print("start task")
                click(main_task_x, main_task_y)
        click(yes_x, yes_y, clicks=4, interval=0.2)

        click_image(NEXT_NEXT, attempts=1, clicks=4)
        click(yes_x, yes_y, clicks=4, interval=0.2)
        click_image(ACCEPT_TASK, attempts=1)
        click_image(FINISH, attempts=1)
        click_image(RECEIVE_AWARD, attempts=1)


def main_entry_2():
    go_home()

    daily_task_accounts = []
    daily_task_accounts.append(SHUANGDAO)
    daily_task_accounts.append(SHESHOU)
    daily_task_accounts.append(ZHANSHEN)
    daily_task_accounts.append(CHUANZHANG)
    daily_task_accounts.append(ZHUJIAO)
    daily_task_accounts.append(FASHI)
   # start_all(daily_task_accounts)

    accounts = []
    accounts.append(SHUANGDAO)
    #accounts.append(SHESHOU)
    #accounts.append(ZHANSHEN)
    accounts.append(CHUANZHANG)
    accounts.append(ZHUJIAO)
    #accounts.append(FASHI)
  #  start_all_hundun(accounts)

    accounts = []
    accounts.append(ZHUJIAO)
    accounts.append(SHUANGDAO)

    #accounts.append(SHESHOU)
    #accounts.append(ZHANSHEN)
    accounts.append(CHUANZHANG)

    # accounts.append(FASHI)
    start_all_yuanzheng(accounts)

    # use_coupon()
    print("Done")

    # receive_mails()
    # click_image(MAX)
    # upgrade_weapon()

    # find_image_on_screen(SWITCH_ACCOUNT_ICON)
    # find_image_on_screen(TASK_ICON)
    # find_image_on_screen(NO_IMAGE)
    # click_image(NO_IMAGE)

    # shoot(total_time=250)
    time.sleep(2)
    # click_image(EXPERIENCE)
    # pyautogui.press("g", presses=250, interval=0.3)

    # test_shoot()
    # click_game_frame()
    # test_task_start_pyramid_task()
    # test_task_start_cook_task()
    # test_task_start_elite_task()
    # test_task_start_ggglden_fish()
    # test_task_start_material_task()
    # test_task_start_weekly_task()
    # test_task_start_wulin_task()
    # test_task_start_upgrade_task()
    # test_task_start_juntuan_task1()

    # test_shoot()
    # test_walk()
    # test_task()


RIGHT_BOTTOM = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/right_bottom.png'

RIGHT_TOP = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/right_top.png'
# Press the green button in the gutter to run the script.
auto_task_x, auto_task_y = 304, 547
add_time_page = '/Users/xinpid/Documents/old/Project_old/MapleStoryAutoRun/resource/add_time_page.png'
add_time_x, add_time_y = 663, 368
def add_time():
    go_home()
    click(x=auto_task_x, y =auto_task_y)
    time.sleep(0.5)
    if not find_image_on_screen(add_time_page):
        go_home()
    click(x=auto_task_x, y=auto_task_y)
    time.sleep(0.5)
    click(x=add_time_x, y=add_time_y, clicks=2)
    time.sleep(0.5)
    pyautogui.press("esc")




if __name__ == '__main__':
    click_game_frame()
    # use_item_before()
    # receive_mails()
    # start_gonghui()
    # click_image(WEEKLY_TASK)
    # find_image_on_screen(MONSTER_ENTER)
    # test_task_start_monster_task()
    main_entry_2()
    #use_coupon()
    #shoot()

# find_image_on_screen(RIGHT_TOP, region=(0, 70*2, 950*2, 600*2))
# auto_run_task(total_time=60 * 30)
# go_task_page()
# test_task_start_monster_task()
