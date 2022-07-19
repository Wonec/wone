# FPS PlayerMovment(Script)

## 获取角色控制器组件

``` csharp
private CharacterController controller;

void Start()
{
    controller = GetComponent<CharacterController>();
}
```

## 移动实现

声明 public float speed 变量用来控制人物移动速度

``` csharp
public float speed;

void Update()
{
    speed = Input.GetKey(KeyCode.leftShift) ? 15f : 10f;
    Movement();
}
void Movement()
{
    // 获取键盘输入
    float x = Input.GetAxis("Horizontal");
    float z = Input.GetAxis("Vertical");
  
    // 将键盘输入值生成一个朝向摄像头的三维向量 并使用Move()方法进行移动
    Vector3 dir = transform.right * x + transform.forward * z;
    controller.Move(dir * speed * Time.deltaTime);
}
```

## 重力实现

在完成基本控制后 在坡度测试场景中发现人物上坡后会保持当前高度 不会下落

这里需要我们自己实现重力的控制

首先声明一个 **public float gravity 变量用来控制重力**

在Player中 **新建一个空对象 置于角色下方 命名为GroundCheck** 用来当作检测点

**新建一个图层命名为Ground 将地面设置为该图层**

声明变量 **public Transform groundCheck 与 public LayerMask ground **

**在Unity编辑器中接收groundCheck的位置与Ground图层**

声明 **public bool isGrounded 变量用来判断是否接触地面**

声明一个 **三维向量velocity 用来获取重力**

``` csharp
public float gravity;

public bool isGrounded;

public Transform groundCheck;

public LayerMask ground;

Vector3 velocity;

void Update()
{		
    // 使用CheckSphere创建球形的检测区域(检测点, 球形半径, 检测图层)
    isGrounded = Physics.CheckSphere(groundCheck.position, 0.5f, ground); 

    Gravity();
}

void Gravity()
{
    // 重力加速度为时间的平方这里乘以两个Time.deltaTime 使用Move方法施加力
    velocity.y += gravity * Time.deltaTime;
    controller.Move(velocity * Time.deltaTime);

    // 这里的重力会不断增加 所以需要在接触地面时给他设置一个适当的值
    if (isGrounded && velocity.y <= 0)
    {
        velocity.y = -2f;
    }
}
```



## 跳跃实现

声明 float值 jumpHeight 变量控制人物跳跃高度 

声明 bool值 jumpPressed 判断是否按下跳跃键

有个小问题在跳跃上物体时会有卡顿现象 是因为CharacterController的角度限制

在跳跃时需要将角度跳大一点方便上斜坡 在接触地面时设置为初始角度

``` csharp
void Update()
{
    // 在Update中进行判断 这里如果使用 jumpPressed = Input.GetButtonDown("Jump") 可能会导致跳跃不灵敏
    if (Input.GetButtonDown("Jump")) {jumpPressed = true;}

    Gravity();
    Jump();
}

void Jump()
{
    if (isGrounded && jumpPressed)
    {
        // 调整坡度限制
        controller.slopeLimit = 100f;
        velocity.y = Mathf.Sqrt(jumpHeight * -2 * gravity); // 模拟跳跃力
        jumpPressed = false;
    }
}

void Gravity()
{
    if (isGrounded && velocity.y <= 0f)
    {
        // 恢复坡度限制
        controller.slopeLimit = 45f;
        velocity.y = -2f;
    }
}
```

到这里FPS基本的人物控制都已经实现 **别忘了公开的变量需要在Unity编辑器中进行赋值**

## 补充(二段跳的实现)

**声明一个int值 jumpCount 控制跳跃的次数**

``` csharp
public int jumpCount = 2;

void Update()
{
    if (Input.GetButtonDown("Jump") && jumpCount > 0) {jumpPressed = true;}
}

void Jump()
{
    if (isGround && jumpPressed)
    {
        controller.slopeLimit = 100f;
        velocity.y = Mathf.Sqrt(jumpHeight * -2 * gravity);
        jumpCount--; // 减少跳跃次数
        jumpPressed = false;
    }
    // (多段跳) 在空中 并且 按下跳跃 并且 跳跃次数大于0 
    if (!isGrounded && jumpPressed && jumpCount > 0)
    {
        // 再次施加跳跃力
        velocity.y = Mathf.Sqrt(jumpHeight * -2 * gravity);
        jumpCount--; // 减少跳跃次数
        jumpPressed = false;
    }
}

void Gravity()
{
    // 在接触地面时将jumpCount恢复
    if (isGrounded && velocity.y <= 0f)
    {
        jumpCount = 2;
    }
}
```

## 补充(跳跃撞天花板不会立马落地解决方法)

在Player中 **新建一个空对象 置于角色头部位置 命名为CeilingCheck** 用来当作检测点

**声明变量 public Transform ceilingCheck 在Unity编辑器中对其赋值**

**声明bool值 isCeiling 判断是否碰撞天花板**

``` csharp
public Transform ceilingCheck;
public bool isCeiling;

void Update()
{
    isCeilinged = Physics.CheckSphere(ceilingCheck.position, 0.5f, ground); // 检测是否碰撞天花板
}

void Gravity()
{
    if (isCeilinged) { velocity.y = 0f; } // 当碰撞到天花板结束向上的力
} 
```



## 补充(推力 只对带有rigidbody的物体有效)

**声明一个float值 impactForce 用来控制推力的大小**

``` csharp
// 内置函数
void OnControllerColliderHit(ControllerColliderHit hit)
{
    // 当碰撞到的物体的rigidbody不为空
    if (hit.rigidbody != null)
        // 添加一个与玩家相反的力
        hit.rigidbody.AddForce(-hit.normal * impactForce);
}
```



## 完整代码

``` csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    private CharacterController controller;

    [Header("基本参数")]
    public float speed = 10f;
    public float gravity = -9.81f;
    public float jumpHeight = 3f;
    public float impactForce = 5f;
    public int jumpCount = 2;

    [Header("状态")]
    public bool isGrounded;
    public bool isCeilinged;
    public bool jumpPressed;

    [Header("环境检测")]
    public Transform groundCheck;
    public Transform ceilingCheck;
    public LayerMask ground;

    Vector3 velocity;

    // Start is called before the first frame update
    void Start()
    {
        controller = GetComponent<CharacterController>();
    }

    // Update is called once per frame
    void Update()
    {
        isGrounded = Physics.CheckSphere(groundCheck.position, 0.5f, ground);
        isCeilinged = Physics.CheckSphere(ceilingCheck.position, 0.5f, ground);
        speed = Input.GetKey(KeyCode.LeftShift) ? 15f : 10f;

        if (Input.GetButtonDown("Jump") && jumpCount > 0) { jumpPressed = true; }

        Movement();
        Gravity();
        Jump();

    }

    // 移动
    void Movement()
    {
        float x = Input.GetAxis("Horizontal");
        float z = Input.GetAxis("Vertical");

        Vector3 dir = transform.right * x + transform.forward * z;
        controller.Move(dir * speed * Time.deltaTime);
    }

    // 重力
    void Gravity()
    {
        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);

        if (isGrounded && velocity.y <= 0f)
        {
            jumpCount = 2;
            controller.slopeLimit = 45f;
            velocity.y = -2f;
        }
        if (isCeilinged) { velocity.y = -2f; }

    }

    // 跳跃
    void Jump()
    {
        if (isGrounded && jumpPressed)
        {
            controller.slopeLimit = 100f;
            velocity.y = Mathf.Sqrt(jumpHeight * -2 * gravity);
            jumpCount--;
            jumpPressed = false;
        }
        // 二段跳
        if (!isGrounded && jumpPressed && jumpCount > 0)
        {
            velocity.y = Mathf.Sqrt(jumpHeight * -2 * gravity);
            jumpCount--;
            jumpPressed = false;
        }
    }

    // 推力(只对带有RigidBody的对象有效)
    void OnControllerColliderHit(ControllerColliderHit hit)
    {
        if (hit.rigidbody != null)
            hit.rigidbody.AddForce(-hit.normal * impactForce);
    }

}
```









