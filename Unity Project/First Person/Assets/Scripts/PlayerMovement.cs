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
