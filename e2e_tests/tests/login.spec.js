// tests/login.spec.js
const { test, expect } = require('@playwright/test');

test.describe('Login Page Tests', () => {
  test('should load the login page', async ({ page }) => {
    await page.goto('https://example.com/login');
    await expect(page).toHaveTitle(/Login/);  // 检查页面标题包含“Login”
  });

  test('should display error for invalid login', async ({ page }) => {
    await page.goto('https://example.com/login');

    // 输入无效的用户名和密码
    await page.fill('input[name="username"]', 'invalidUser');
    await page.fill('input[name="password"]', 'wrongPassword');
    await page.click('button[type="submit"]');

    // 检查是否显示错误消息
    const errorMessage = await page.locator('.error-message');
    await expect(errorMessage).toBeVisible();
    await expect(errorMessage).toHaveText('Invalid username or password');
  });

  test('should log in with valid credentials', async ({ page }) => {
    await page.goto('https://example.com/login');

    // 输入有效的用户名和密码
    await page.fill('input[name="username"]', 'validUser');
    await page.fill('input[name="password"]', 'correctPassword');
    await page.click('button[type="submit"]');

    // 检查是否成功登录，假设登录后重定向到主页
    await expect(page).toHaveURL('https://example.com/home');
  });
});
