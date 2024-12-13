# Cortex E2E Tests
We use open-source E2E automation framework called [Playwright](https://playwright.dev/) for project E2E.

# How to Setup Testing Env
1. In your terminal, go to `cortex_e2e_tests[]()`folder.

```
cd ~/unitx_repos/project_template/e2e_tests
```

If already have `node_modules`, remove it.
```
rm -rf node_modules
```
<br>

2. Install packages.
```
npm install
```
> [!NOTE]
> Using `yarn install` might not resolve dependency issues here.

<br>

3. Install the testing data from S3.


> [!NOTE]
> If you encounter a permission issue, please ask your manager for aws permission.

<br>

> [!NOTE]
> Because of record mismatch of central db, you might see errors on production data page.
When we add e2e tests for production data page, we should have a better way to handle it.


<br>

<br>

# How to Run E2E
1. In your terminal, go to `cortex_e2e_tests`folder.

```
cd ~/unitx_repos/project_template/e2e_tests
```

<br>

2. Run the following command.
```
npx playwright test
```

If you want to use [UI mode](https://playwright.dev/docs/test-ui-mode), run
```
npx playwright test --ui
```
> [!NOTE]
> UI window there doesn't show our app's screen, because it doesn't support AppImage.

If you want try the actual way of what CI does,

(1) Install xvfb.
```
sudo apt-get upgrade

sudo apt-get xvfb
```

(2) Run test on the top of xvfb.
```
xvfb-run --auto-servernum --server-args="-screen 0 1280x720x24" -- npx playwright test
```

> [!NOTE]
> [Xvfb](https://en.wikipedia.org/wiki/Xvfb) is a software that makes a virtual display of X Window System.