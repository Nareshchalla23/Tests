import { test, Page } from '@playwright/test';

async function createClickIndicator(page: Page, x: number, y: number) {
  await page.evaluate(({ x, y }) => {
    const indicator = document.createElement('div');
    indicator.style.position = 'absolute';
    indicator.style.left = `${x}px`;
    indicator.style.top = `${y}px`;
    indicator.style.width = '20px';
    indicator.style.height = '20px';
    indicator.style.borderRadius = '50%';
    indicator.style.backgroundColor = 'rgba(0, 0, 255, 0.5)'; // Blue for right-clicks
    indicator.style.pointerEvents = 'none';
    indicator.style.transition = 'opacity 1s';
    indicator.style.zIndex = '9999';
    document.body.appendChild(indicator);

    setTimeout(() => {
      indicator.style.opacity = '0';
      setTimeout(() => indicator.remove(), 1000);
    }, 1000);
  }, { x, y });
}

async function performRandomRightClick(page: Page) {
  const viewportSize = await page.viewportSize();
  if (!viewportSize) return;

  const x = Math.floor(Math.random() * viewportSize.width);
  const y = Math.floor(Math.random() * viewportSize.height);

  await createClickIndicator(page, x, y);
  await page.mouse.click(x, y, { button: 'right' });
}

test('Open Google and perform random right-clicks for 6 hours', async ({ page }) => {
  test.setTimeout(6 * 60 * 60 * 1000);

  await page.goto('https://www.google.com');

  const sixHoursInMs = 6 * 60 * 60 * 1000;
  const interval = 5000; // 5 seconds

  const endTime = Date.now() + sixHoursInMs;

  while (Date.now() < endTime) {
    await performRandomRightClick(page);
    await page.waitForTimeout(interval);
  }
});
