# Examples

Read this file when the source is longer than a few steps, or when a draft fails the check.

## Procedure

Source:

> To rotate the key you will need to first make sure that you have admin access and then you can leverage the dashboard in order to create a new key, and you should also revoke the old one as well as update the workers so that they are using the new secret.

Draft:

```markdown
# Rotate the API key

An admin can replace the API key.
The workers then use the new secret.

## Before you start

You need the admin role on the project.

## Steps

1. Open the project dashboard.
2. Create a new API key.
3. Store the key in the worker secret.
4. Restart the workers.
5. Revoke the old API key.

Revoke the old key only after the workers restart. A worker that still has the old key will fail closed.
```

## Dense explanation

Source:

> The cache invalidation path is essentially a best-effort fan-out. When a write is committed, the primary publishes an invalidation event onto the bus, and then each node independently drops its local entry if it happens to have one. It is important to note that there is no acknowledgement, so a partitioned node can serve stale data until its TTL expires. The system does not try to be strongly consistent here.

Draft:

```markdown
# Cache invalidation

An operator can predict when a node serves stale data after a write.

## What a write does

The primary commits the write. Then the primary publishes one invalidation event on the bus.

Each node that receives the event deletes its local entry for that key. A node that has no entry ignores the event.

## What a partitioned node does

The bus does not collect an acknowledgement. A node that misses the event keeps its entry until the TTL ends. During that time the node can serve stale data.

This path does not provide strong consistency.
```

## Dictionary pair

Not STE: "Ensure the switch is off prior to commencing the test."

STE: "Make sure that the switch is off before you start the test."

"you" is allowed. "Make sure", "before", and "start" are the approved words from the sheet.

## Safety line

```markdown
WARNING: Do not touch the brake unit until it is cool. Hot parts can cause injury.
```

`WARNING` means a risk of injury. `CAUTION` means a risk of damage. The command comes before the risk.
