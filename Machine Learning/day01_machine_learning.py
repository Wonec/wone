from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import jieba


def datasets_demo():
    """
    sklearn数据集使用
    """
    # 获取数据集
    iris = load_iris()  # 返回的是 datasets.base.Bunch(继承自字典)
    print("鸢尾花数据集: \n", iris)
    print("查看数据集描述: \n", iris["DESCR"])
    print("查看特征值的名字: \n", iris.feature_names)
    print("查看特征值: \n", iris.data, iris.data.shape)

    # 数据集的划分
    # 训练集特征、目标, 测试集特征、目标
    # train_test_split(特征数据数组, 标签数组, 测试集大小float值, 随机数种子  )
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=22
    )
    print("训练集的特征值: \n", x_train, x_train.shape)

    return None


def dict_demo():
    """
    字典特征提取
    """
    data = [
        {"city": "北京", "temperature": 100},
        {"city": "上海", "temperature": 60},
        {"city": "深圳", "temperature": 30},
    ]
    # 1、实例化一个转换器类 sparse -> 稀疏矩阵
    transfer = DictVectorizer(sparse=True)

    # 2、调用fit_transform()
    data_new = transfer.fit_transform(data)
    print("data_new: \n", data_new.toarray(), type(data_new))
    print("特征名字: \n", transfer.get_feature_names())

    return None


def count_demo():
    """
    文本特征提取CountVectorizer
    """
    data = [
        "life is short, i like python",
        "life is too long, i dislike python"
    ]
    # 1. 实例化 一个转换器类
    transfer = CountVectorizer(stop_words=['is', 'too'])

    # 2. 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new: \n", data_new.toarray())
    print("特征名字: \n", transfer.get_feature_names())

    return None


def count_chinese_demo():
    """
    文本特征提取CountVectorizer
    """
    data = [
        "我 爱 北京 天安门",
        "天安门 上 太阳 升"
    ]
    # 1. 实例化 一个转换器类
    transfer = CountVectorizer()

    # 2. 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new: \n", data_new.toarray())
    print("特征名字: \n", transfer.get_feature_names())

    return None


def count_chinese_demo2():
    """
    中文文本特征抽取自动分词
    """

    data = [
        "一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
        "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去",
        "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取決于如何将其与我们所了解的事物相联系。"
    ]

    index = 0
    for sent in data:
        data[index] = cut_word(sent)
        index += 1

    # 实例化一个转换器的类
    transfer = CountVectorizer(stop_words=["一种", "所以"])

    # 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new: \n", data_new.toarray())
    print("特征名字: \n", transfer.get_feature_names())

    return None


def cut_word(text):
    """
    进行中文分词 "我爱北京天安门" --> "我 爱 北京 天安门"
    """

    return " ".join(list(jieba.cut(text)))


if __name__ == "__main__":
    # 代码1: sklearn数据集使用
    # datasets_demo()
    # 代码2: 字典特征提取
    # dict_demo()
    # 代码3：文本特征提取
    # count_demo()
    # 代码4：中文文本特征抽取
    # count_chinese_demo()
    # 代码5：中文文本特征提取2
    count_chinese_demo2()
