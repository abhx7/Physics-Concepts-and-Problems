% Boundary Conditions
x1 = 0; y1 = 1; % Start point
x2 = 2; y2 = 0; % End point
delta_x = x2 - x1;
delta_y = y1 - y2;

% Define the function to solve for theta_end
equations = @(theta_end) ...
    (delta_y / (1 - cos(theta_end))) * (theta_end - sin(theta_end)) - delta_x;

% Solve for theta_end
theta_end = fzero(equations, pi);

% Compute radius r
r = delta_y / (1 - cos(theta_end));

fprintf('Radius (r): %.4f\n', r);
fprintf('Final Angle (theta_end): %.4f radians\n', theta_end);

% Generate Cycloid Parameterization
theta = linspace(0, theta_end, 100);
x = r * (theta - sin(theta)) + x1; % Offset to start at x1
y = y1 - r * (1 - cos(theta)); % Offset to start at y1

% Visualization of the Brachistochrone Curve
figure;
plot(x, y, 'b-', 'LineWidth', 2); hold on;
scatter([x1, x2], [y1, y2], 100, 'r', 'filled'); % Points A and B
text(x1, y1, '  Start (A)', 'FontSize', 12, 'Color', 'red', 'FontWeight', 'bold');
text(x2, y2, '  End (B)', 'FontSize', 12, 'Color', 'red', 'FontWeight', 'bold');
title('Brachistochrone Problem Solution');
xlabel('x');
ylabel('y');
grid on;
legend({'Brachistochrone Curve', 'Points A and B'}, 'Location', 'best');
hold off;
