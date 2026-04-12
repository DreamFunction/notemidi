# easy_scamp

#### 介绍
easy_scamp - 人性化旋律转 SCAMP 格式。写音乐就像 [('C4',4), ('E4',4), ('r',2)]，直接得到 (MIDI 编号, 秒数)。

#### 安装教程

1. 确保已安装 SCAMP：`pip install scamp`
2. 将 `easy_scamp.py` 下载到你的项目目录中
3. 或者直接复制代码使用


#### 使用说明

**本模块的核心是`translate`函数**（如果确实有相应需求，你也可以用其他函数，但是平常`translate`够用了）,你可以在模块内找到一个DEFAULT常量，它的值就是'translate'。

def translate(mlist, bpm=120, wnote=4):

    将人性化旋律列表转换为 SCAMP 可用的 (MIDI 音高, 秒数) 列表。
    
    参数:
        mlist: 列表，每个元素为 (音符名, 时值) 元组
            音符名: 'C4', 'c4', 'F#3', 'r', 'R', None 或 MIDI 数字
            时值: 数字 (4=四分, 8=八分) 或 字符串 ('4.'=附点, '2+2+4'=加法)
        bpm: 每分钟拍数，默认 120
        wnote: 全音符拍数，默认 4（即 4/4 拍）
    
    返回:
        [(midi, seconds), ...] 列表，休止符的 midi 为 None
    
    异常:
        TypeError: 输入类型错误
        ValueError: 时值不合法或元组长度不为2
        KeyError: 未知音符名



#### 异常对照表


| 位置 | 中文 | 英文 |
|------|--------|----------|
| `translate_dot` | `"时值字符串必须是数字"` | `"Duration string must be digits followed by '.'"` |
| `translate_dot` | `"时值必须大于零"` | `"Duration must be greater than zero"` |
| `translate_duration` | `"时值必须是数字"` | `"Duration must be a number"` |
| `translate_duration` | `"时值必须大于零"` | `"Duration must be greater than zero"` |
| `translate_note` | `"音符名必须是字符串或数字或None"` | `"Note name must be a string, number, or None"` |
| `translate_note` | `"音符名不存在"` | `"Note name not found"` |
| `translate_tie` | `"你是不是连写了两个“+”或在开头或结尾直接写了“+”"` | `"Invalid tie expression: consecutive '+', leading/trailing '+'"` |
| `translate_tie` | `"时值字符串必须是数字"` | `"Duration string must be a number or dotted (e.g., '4.')"` |
| `translate_tie` | `"时值必须大于零"` | `"Duration must be greater than zero"` |
| `translate` | `"音乐列表必须是列表"` | `"Music list must be a list"` |
| `translate` | `"每分节拍数必须是数字"` | `"bpm must be a number"` |
| `translate` | `"全音符拍数必须是数字"` | `"wnote must be a number"` |
| `translate` | `"音乐列表的元素必须是元组"` | `"Each element of music list must be a tuple"` |
| `translate` | `"音乐列表内的元组长度必须是2"` | `"Each tuple must have length 2 (note, duration)"` |
| `translate` | `"时值字符串不合法"` | `"Invalid duration string"` |

#### 其他函数使用说明

def translate_dot(dur, bpm=120, wnote=4):

    将附点时值字符串（如 '4.'）转换为秒数。
    
    参数:
        dur: 附点时值字符串，例如 '4.' 表示附点四分音符
        bpm: 每分钟拍数（beats per minute）
        wnote: 全音符的拍数（默认4，即4/4拍）
    
    返回:
        对应的秒数
    
    异常:
        TypeError: 时值字符串格式不正确（不是数字后跟点号）
        ValueError: 时值 <= 0

def translate_duration(dur, bpm=120, wnote=4):

    将普通数字时值转换为秒数。
    
    参数:
        dur: 时值数字，例如 4 表示四分音符（以全音符为单位）
        bpm: 每分钟拍数
        wnote: 全音符的拍数（默认4）
    
    返回:
        对应的秒数
    
    异常:
        TypeError: dur 不是数字
        ValueError: dur <= 0

def translate_note(note):

    将音符名转换为 MIDI 音高编号，休止符返回 None。
    
    参数:
        note: 音符名（如 'C4', 'c4', 'F#3'），或 'r'/'R'/None 表示休止，或 MIDI 数字
    
    返回:
        MIDI 音高编号，或 None（休止符）
    
    异常:
        ValueError: 输入类型不是字符串、数字或 None
        KeyError: 音符名不在映射表中

def translate_tie(dur, bpm=120, wnote=4):

    解析加法时值字符串（如 '2+2+4'），返回总秒数。
    
    参数:
        dur: 加法表达式字符串，各部分用 '+' 连接，每部分可以是普通数字或附点字符串
        bpm: 每分钟拍数
        wnote: 全音符的拍数
    
    返回:
        总秒数
    
    异常:
        ValueError: 表达式为空、连续两个 '+'、开头/结尾有 '+'，或某部分非数字/附点

#### 参与贡献

欢迎提交 Issue 或 PR
