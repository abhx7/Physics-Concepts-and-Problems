% Define constants and initial points
A = [0, 50];  % Starting point (0, 50)
B = [60, 0];  % Ending point (60, 0)
g = 9.81;     % Gravitational constant

% Define a parametric cycloid approximation
theta_max = pi;  % Adjust the max angle based on the endpoint
num_points = 100;
theta = linspace(0, theta_max, num_points);

% Cycloid parameters
R = B(2) / (1 - cos(theta_max));  % Radius of the cycloid circle

% Parametric equations for the cycloid
x_cycloid = A(1) + R * (theta - sin(theta));
y_cycloid = A(2) - R * (1 - cos(theta));

% Calculate time of descent using the cycloid approximation
ds = sqrt(diff(x_cycloid).^2 + diff(y_cycloid).^2);  % Path differential elements
velocities = sqrt(2 * g * (A(2) - y_cycloid(1:end-1)));  % Speed along the path
time_of_descent = sum(ds ./ velocities);  % Total descent time

% Display time of descent
fprintf('Optimized time of descent: %.4f seconds\n', time_of_descent);

% Visualization
figure;
hold on;

% Plot the cycloid (fastest descent path)
plot(x_cycloid, y_cycloid, 'r-', 'LineWidth', 2, 'DisplayName', 'Fastest Descent Path');

% Mark starting and ending points
plot(A(1), A(2), 'bo', 'MarkerSize', 8, 'MarkerFaceColor', 'b', 'DisplayName', 'Start Point A');
plot(B(1), B(2), 'go', 'MarkerSize', 8, 'MarkerFaceColor', 'g', 'DisplayName', 'End Point B');

% Formatting
title('Fastest Descent Path (Brachistochrone Curve)');
xlabel('x (horizontal position)');
ylabel('y (vertical position)');
legend;
grid on;
axis equal;

% Final touches
text(A(1), A(2), '  A', 'VerticalAlignment', 'bottom', 'FontWeight', 'bold');
text(B(1), B(2), '  B', 'VerticalAlignment', 'top', 'FontWeight', 'bold');
set(gca, 'FontSize', 12, 'FontWeight', 'bold');

hold off;
