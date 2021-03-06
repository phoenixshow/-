from pymysql import connect

class JD(object):
  def __init__(self):
    # 创建Connection连接
    self.conn = connect(host='localhost',port=3306,user='root',password='123456',database='jing_dong',charset='utf8')
    # 获得Cursor对象
    self.cursor = self.conn.cursor()

  def __del__(self):
    # 关闭Cursor对象
    self.cursor.close()
    # 关闭Connection对象
    self.conn.close()

  def execute_sql(self, sql):
    self.cursor.execute(sql)
    for temp in self.cursor.fetchall():
      print(temp)

  def show_all_items(self):
    """显示所有的商品"""
    sql = "select * from goods;"
    self.execute_sql(sql)

  def show_cates(self):
    sql = "select name from goods_cates;"
    self.execute_sql(sql)
    
  def show_brands(self):
    sql = "select name from goods_brands;"
    self.execute_sql(sql)
    
  def add_cates(self):
    item_name = input("请输入新商品分类的名称：")
    sql = """insert into goods_cates (name) values("%s");""" % item_name
    self.cursor.execute(sql)
    self.conn.commit()
    
  def update_cates(self):
    id = 0
    while True:
      try:
        id = int(input("请输入要修改的商品分类的id："))
      except Exception as ret:
        print("请输入正确的id编号！")
      else:
        break
    item_name = input("请输入新商品分类的名称：")
    sql = """update goods_cates set name="%s" where id="%s";""" % (item_name, id)
    self.cursor.execute(sql)
    self.conn.commit()
    
  def delete_cates(self):
    id = 0
    while True:
      try:
        id = int(input("请输入要删除的商品分类的id："))
      except Exception as ret:
        print("请输入正确的id编号！")
      else:
        break
    isdel = input("您确认要删除编号为%s的商品分类吗？按y确认，其它键返回主菜单：" % id)
    if isdel == "y":
      # 方案一真删：将所有分类下商品的类别置为NULL，再删除分类
      # 方案二假删：添加是否显示该分类的字段，更新该字段为隐藏
      pass

  @staticmethod
  def print_menu():
      print("------京东------")
      print("1：所有的商品")
      print("2：所有的商品分类")
      print("3：所有的商品品牌分类")
      print("4：添加商品分类")
      print("5：修改商品分类")
      print("6：删除商品分类")
      return input("请输入功能对应的序号：")

  def run(self):
    while True:
      num = self.print_menu()
      if num == "1":
        # 查询所有商品
        self.show_all_items()
      elif num == "2":
        # 查询分类
        self.show_cates()
      elif num == "3":
        # 查询品牌分类
        self.show_brands()
      elif num == "4":
        # 添加商品分类
        self.add_cates()
      elif num == "5":
        # 修改商品分类
        self.update_cates()
      elif num == "6":
        # 删除商品分类
        self.delete_cates()
      else:
        print("输入有误，请重新输入……")

def main():
  # 1. 创建一个京东商城对象
  jd = JD()

  # 2. 调用这个对象的run方法，让其运行
  jd.run()

if __name__ == "__main__":
  main()